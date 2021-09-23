import psutil
import time

LOCATION= '../../output/'
file_name = '_cpu_usage.txt'

def measure_compute_activity(pid):
    result = psutil.pid_exists(pid)
    if False == result :
        print("Process ID doesn't exist")

    my_file = open(LOCATION + str(pid) + file_name, 'w')

    while result == True:

        p = psutil.Process(pid)
        cpu_percent_util = p.cpu_percent(interval=0.1)
        result = psutil.pid_exists(pid)
        output_activity = str(time.time()) + "," + str(cpu_percent_util)
        my_file.write(output_activity + "\n")
        time.sleep(0.1)

    my_file.close()
