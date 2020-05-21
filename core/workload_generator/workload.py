import download_file, disk_usage

'''
Starts the disk related and network related scripts
'''
def workload_begin():
    download_file.download_file_from_network()
    disk_usage.read_files_from_local_disk()

'''
Start the workload
'''
workload_begin()