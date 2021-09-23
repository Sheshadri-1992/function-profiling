#!/bin/bash

if [ "$#" -ne 1 ]; then
   echo "usage : bash execute_profile.sh  <pid>"
   exit
fi


_pid=$1
echo "The pid is "$_pid
python ./core/measure_activity.py $_pid
