#!/bin/bash
# run_all.sh
# Usage: ./run_all.sh N_CORES
set -euo pipefail
trap "echo 'Stopping...'; kill 0" SIGINT SIGTERM

NCORES=${1:-}
[ -z "$NCORES" ] && { echo "Usage: $0 N_CORES"; exit 1; }

mkdir -p logs

# launch a python job pinned to a core
run_task() {
  local core="$1" name="$2" code="$3" log="logs/${name}.log"
  echo "$name -> core $core | $log"
  taskset -c "$core" python - <<END >"$log" 2>&1
$code
END
}

# wait for a batch and collect statuses
wait_batch() {
  local -n _pids=$1
  local -n _names=$2
  local -n _statuses=$3
  for idx in "${!_pids[@]}"; do
    pid="${_pids[$idx]}"
    name="${_names[$idx]}"
    if wait "$pid"; then
      _statuses["$name"]=0
    else
      _statuses["$name"]=$?
    fi
  done
  _pids=()
  _names=()
}

# collect tasks
tasks=()

# stations -> process_l2_l3
stations=$(python - <<'END'
import pandas as pd, numpy as np
df = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
print(" ".join(np.unique(df["station_id"].to_numpy())))
END
)
for st in $stations; do
  tasks+=("station_${st};from test_processing_scripts import process_l2_l3; process_l2_l3('${st}')")
done

# sites -> join_l3
sites=$(python - <<'END'
import pandas as pd, numpy as np
df = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
print(" ".join(np.unique(df["site_id"].to_numpy())))
END
)
for site in $sites; do
  tasks+=("site_${site};from test_processing_scripts import join_l3; join_l3('${site}')")
done

# run with at most NCORES concurrent jobs, gather exit statuses
i=0
pids=()
names=()
declare -A status_map

for task in "${tasks[@]}"; do
  name="${task%%;*}"
  code="${task#*;}"
  core=$(( i % NCORES ))

  # launch
  ( run_task "$core" "$name" "$code" ) &
  pids+=($!)
  names+=("$name")

  # wait for a full batch
  if (( (i+1) % NCORES == 0 )); then
    wait_batch pids names status_map
  fi
  i=$((i+1))
done

# wait remaining
if ((${#pids[@]})); then
  wait_batch pids names status_map
fi

# summary
echo
echo "===== Summary ====="
ok=0; fail=0
for name in "${!status_map[@]}"; do
  code=${status_map[$name]}
  if [ "$code" -eq 0 ]; then
    printf "[OK]   %s\n" "$name"
    ok=$((ok+1))
  else
    printf "[FAIL] %s (exit %d)  -> logs/%s.log\n" "$name" "$code" "$name"
    fail=$((fail+1))
  fi
done
echo "Done. OK=$ok  FAIL=$fail"
