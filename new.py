import socket
import threading
import time
import pyfiglet
from queue import Queue
#target = <"IP">or<"url">
#target = "iiitmk.ac.in"
target = str(input("Enter the Host to Scan : "))
queue=Queue()
open_ports = []
def portscanner(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target,port))
        return True
    except:
        return False
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)
def worker():
    while not queue.empty():
        port=queue.get()
        if portscanner(port):
            print("Port {} is open".format(port))
            open_ports.append(port)
        #else:
            #print("Port {} is closed".format(port))
port_list= range(1,500)
fill_queue(port_list)
thread_list=[]
for t in range(100):
    thread=threading.Thread(target=worker)
    thread_list.append(thread)
for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()    
print("Open ports are,",open_ports) 
