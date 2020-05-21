import time

LOCATION = "/home/swamiji/phd/csl/serverless_computing/function_profiling/sample_read_files/"

def read_files_from_local_disk():
    for i in range(1,10):
        filename = LOCATION+str(i)+".txt"
        fd = open(filename,'r')
        msg = fd.read()
        print("File read ",i,"size of message ",len(msg))
        fd.close()
        time.sleep(1)