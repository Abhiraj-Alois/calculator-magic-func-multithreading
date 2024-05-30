import threading 
import time

semaphore = threading.BoundedSemaphore(value = 5)

def access(thread_number):
    print(f"{thread_number} is trying to access the file")
    semaphore.acquire()
    print(f"{thread_number} was granted access")
    time.sleep(1)
    print(f"{thread_number} was released")
    semaphore.release()
    
for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
    