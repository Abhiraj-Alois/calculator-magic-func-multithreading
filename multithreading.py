import threading

def f1():
    for i in range(1000):
        print('ONE')
        
def f2():
    for i in range(1000):
        print('TWO')
        
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
# t1.join()
t2.start()