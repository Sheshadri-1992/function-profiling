#!/bin/bash

# program which causes disk activity
#python disk_usage.py >raw_disk_output.txt 2>&1 &

# previously existing commands
# python disk_usage.py >/dev/null 2>&1 &

# program which causes network activity
#python ./core/workload_generator/workload.py >raw_output.txt 2>&1 &
#_pid=$!

if [ "$#" -ne 1 ]; then
    echo "Need a pid: Usage => bash execute_profile.sh <pid>"
    exit 0;
fi

_pid=$1

echo "The pid is "$_pid
python3.6 ./core/measure_activity.py $_pid
