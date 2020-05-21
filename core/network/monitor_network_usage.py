import psutil
import subprocess

LOCATION = "/home/swamiji/phd/csl/serverless_computing/function_profiling/core/network/"
SCRIPT = "network_activity_measure.sh"

def check_network_activity(pid):
    result = psutil.pid_exists(pid)
    if result == True:
        subprocess.call(['bash', LOCATION + SCRIPT, str(pid)])
    return "completed"