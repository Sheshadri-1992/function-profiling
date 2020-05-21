#!/bin/bash

if [ "$#" -ne 1 ]; then
   echo "usage : bash network_activity_measure.sh pid"
   exit
fi

# Capture the pid
_pid=$1
echo "[bash] The pid is "$_pid

# Capture the network activity
sudo nethogs -t -c 10 | grep $_pid >> $_pid"_network_raw_logs.txt"

# inline replace of files using sed
sed -i -e 's/[[:space:]]\+/ /g' $_pid"_network_raw_logs.txt"
awk '{print $2","$3","$2+$3}' $_pid"_network_raw_logs.txt" > $_pid"_network_usage.txt"
