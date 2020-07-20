import sys
from multiprocessing import Process
import psutil

from network import monitor_network_usage
from disk import monitor_disk_usage
from compute import monitor_compute_usage
from memory import monitor_memory_usage

'''
Executes a script which captures the network usage process-id 
'''


def network_activity(pid):
    try:
        monitor_network_usage.check_network_activity(pid)
    except:
        print("Exception caught in network activity")


'''
Measure the disk activity performed by process-id
url: https://stackoverflow.com/questions/49357887/how-to-get-current-disk-io-and-network-io-into-percentage-using-python
'''


def disk_activity(pid):
    try:
        monitor_disk_usage.measure_disk_activity(pid)
    except:
        print("Exception caught in disk activity")

'''
Measure the cpu activity of the program
'''


def cpu_activity(pid):
    try:
        monitor_compute_usage.measure_compute_activity(pid)
    except:
        print("Exception caught in compute activity")

'''
Measure the memory usage of the program
'''


def memory_activity(pid):
    try:
        monitor_memory_usage.measure_memory_activity(pid)
    except:
        print("Exception caught in memory activity")

'''
Measure the different aspects of program
'''


def measure_total_activity(pid):
    result = psutil.pid_exists(pid)
    if result == True:
        disk_process = Process(target = disk_activity, args = (pid,))
        network_process = Process(target = network_activity, args = (pid,))
        cpu_process = Process(target=cpu_activity, args = (pid,))
        memory_process = Process(target=memory_activity, args = (pid,))

        # Start the monitoring processes
        disk_process.start()
        network_process.start()
        cpu_process.start()
        memory_process.start()

        # Wait till all the monitoring processes ends
        disk_process.join()
        network_process.join()
        cpu_process.join()
        memory_process.join()


if len(sys.argv) != 2:
    exit(0)

'''
Starting point for the code
'''
measure_total_activity(int(sys.argv[1]))

'''
Testing with some pid
'''
# measure_total_activity(int(5555))