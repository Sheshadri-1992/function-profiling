import psutil
import time

LOCATION= '/home/swamiji/phd/csl/serverless_computing/function_profiling/output/'
file_name = '_memory_usage.txt'

def measure_memory_activity(pid):
    result = psutil.pid_exists(pid)
    if False == result :
        print("Process ID doesn't exist")

    my_file = open(LOCATION + str(pid) + file_name, 'w')

    while result == True:

        p = psutil.Process(pid)
        memory_percent_util = p.memory_percent()
        result = psutil.pid_exists(pid)
        output_activity = str(time.time()) + "," + str(memory_percent_util)
        my_file.write(output_activity + "\n")
        time.sleep(0.1)

    my_file.close()