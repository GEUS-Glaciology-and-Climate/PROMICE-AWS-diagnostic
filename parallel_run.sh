#!/bin/bash
# run_all.sh
# Usage: ./run_all.sh N_CORES

NCORES=$1
if [ -z "$NCORES" ]; then
  echo "Usage: $0 N_CORES"
  exit 1
fi

###############################################
# 1. Run process_l2_l3 for all station_id
###############################################
stations=$(python - <<'END'
import pandas as pd, numpy as np
df = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
stations = np.unique(df["station_id"].to_numpy())
print(" ".join(stations))
END
)

i=0
for st in $stations; do
  core=$(( i % NCORES ))
  echo "Launching process_l2_l3 for $st on core $core"
  taskset -c $core python - <<END &
from mymodule import process_l2_l3
process_l2_l3("${st}")
END
  i=$((i+1))
done

###############################################
# 2. Run join_l3 for all site_id
###############################################
sites=$(python - <<'END'
import pandas as pd, numpy as np
df = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
sites = np.unique(df["site_id"].to_numpy())
print(" ".join(sites))
END
)

j=0
for site in $sites; do
  core=$(( j % NCORES ))
  echo "Launching join_l3 for $site on core $core"
  taskset -c $core python - <<END &
from mymodule import join_l3
join_l3("${site}")
END
  j=$((j+1))
done

# wait for all background jobs
wait
echo "All stations and sites processed."
