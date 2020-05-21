import requests
import time
PATH = "/home/swamiji/phd/csl/serverless_computing/function_profiling/download_location/"
url = 'http://www.africau.edu/images/default/sample.pdf'

def download_file_from_network():
    for i in range(20):
        my_file = requests.get(url, allow_redirects=True)
        file_name = "sample"+str(i)+".pdf"
        open(PATH+file_name, 'wb').write(my_file.content)
        print("The file download_location is written to ",file_name)
        time.sleep(1)