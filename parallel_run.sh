#!/bin/bash
# run_all.sh
# Usage: ./run_all.sh N_CORES
set -euo pipefail

NCORES=${1:-}
[ -z "$NCORES" ] && { echo "Usage: $0 N_CORES"; exit 1; }

mkdir -p logs

# function to run a python call pinned to a core
run_task() {
  core=$1
  name=$2
  code=$3
  log="logs/${name}.log"
  echo "$name -> core $core | $log"
  taskset -c "$core" python - <<END >"$log" 2>&1
$code
END
}

# collect all tasks (stations + sites)
tasks=()

# stations
stations=$(python - <<'END'
import pandas as pd, numpy as np
df = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
print(" ".join(np.unique(df["station_id"].to_numpy())))
END
)
for st in $stations; do
  tasks+=("station_${st};from mymodule import process_l2_l3; process_l2_l3('${st}')")
done

# sites
sites=$(python - <<'END'
import pandas as pd, numpy as np
df = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
print(" ".join(np.unique(df["site_id"].to_numpy())))
END
)
for site in $sites; do
  tasks+=("site_${site};from mymodule import join_l3; join_l3('${site}')")
done

# run tasks with at most $NCORES concurrent jobs
i=0
pids=()
for task in "${tasks[@]}"; do
  name="${task%%;*}"
  code="${task#*;}"
  core=$(( i % NCORES ))

  run_task "$core" "$name" "$code" &    # launch in background
  pids+=($!)

  # if we have launched NCORES tasks, wait for all before continuing
  if (( (i+1) % NCORES == 0 )); then
    wait "${pids[@]}"
    pids=()
  fi
  i=$((i+1))
done

# wait for any remaining jobs
wait "${pids[@]:-}"

echo "All jobs completed."
