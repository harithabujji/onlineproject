import os,django
import threading

import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE","onlineproject.settings")
django.setup()




from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print("Queue full, producer is waiting")
                condition.wait()
                print("Space in queue, Consumer notified the producer")
            num = random.choice(nums)
            queue.append(num)
            print("Produced", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait()
                print("Producer added something to queue and notified the consumer")
            num = queue.pop(0)
            print("Consumed", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


# ProducerThread().start()
# ConsumerThread().start()


def producer(id):
    global queue
    condition.acquire()
    if len(queue) == MAX_NUM:
        print("Queue full, producer is waiting")
        condition.wait()
        print("Space in queue, Consumer notified the producer")

    queue.append(id)
    print("Produced", id)
    condition.notify()
    condition.release()
    time.sleep(random.random())

def consumer(id):
    global queue
    condition.acquire()
    if not queue:
        print("Nothing in queue, consumer is waiting")
        condition.wait()
        print("Producer added something to queue and notified the consumer")
    num = queue.pop(0)
    print("Consumed",id)
    condition.notify()
    condition.release()
    time.sleep(random.random())


if __name__ == "__main__":
    # threads=[]
    url = "http://127.0.0.1:8000/onlineapp/clg/"
    req=requests.get(url)


    print(req)
    print(req.json())
    for i in req.json():
        p = threading.Thread(target=producer,args=(i['id'],))
        c = threading.Thread(target=consumer, args=(i['id'],))
        p.start()
        c.start()


