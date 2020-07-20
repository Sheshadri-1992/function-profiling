import download_file, disk_usage

def generate_prime():
    lower = 900
    upper = 1000

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               pass

'''
Starts the disk related and network related scripts
'''
def workload_begin():
    download_file.download_file_from_network()
    disk_usage.read_files_from_local_disk()
    print("Generate prime numbers")
    for i in range(0,100):
        generate_prime()

'''
Start the workload
'''
workload_begin()