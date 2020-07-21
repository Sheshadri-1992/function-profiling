import psutil
import time

LOCATION= '../output/'
file_name = '_disk_usage.txt'

def measure_disk_activity(pid):
    result = psutil.pid_exists(pid)
    total_disk_MB = 0
    my_file = open(LOCATION + str(pid) + file_name, 'w')

    while result == True:
        for proc in psutil.process_iter():

            if (proc.pid) == pid:
                io_counters = proc.io_counters()
                total_disk_MB = io_counters[4] + io_counters[5]  # read_chars + write_chars
                # print("Disk-IO => PID: ", proc.pid, "Disk", total_disk_MB, " IO counters ", io_counters)
                output_activity = str(io_counters[4])+","+str(io_counters[5])+","+str(total_disk_MB)
                my_file.write(output_activity+"\n")

        result = psutil.pid_exists(pid)
        time.sleep(1)

    total_disk_MB = float(total_disk_MB / 1000000)
    print("Total disk activity is ", total_disk_MB)
    my_file.close()
