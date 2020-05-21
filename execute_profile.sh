#!/bin/bash

# program which causes disk activity
#python disk_usage.py >raw_disk_output.txt 2>&1 &

# previously existing commands
# python disk_usage.py >/dev/null 2>&1 &

# program which causes network activity
python ./core/workload_generator/workload.py >raw_output.txt 2>&1 &
_pid=$!

echo "The pid is "$_pid
python ./core/measure_activity.py $_pid