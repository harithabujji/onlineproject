


import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","onlineproject.settings")
django.setup()

import requests
from onlineapp.models import *
# Create your tests here.

querysets=Student.objects.values('id','name')
# for qs in querysets:
#     print(qs)


import threading

def f(id):
    child_threads=[]
    req=requests.get("http://127.0.0.1:8000/onlineapp/clgst/"+str(id)+'/')
    print(req.json())
    return




if __name__ == "__main__":
    threads=[]
    req=requests.get("http://127.0.0.1:8000/onlineapp/clg/")
    # print(req.json())
    # import ipdb
    # ipdb.set_trace()
    # for i in querysets:
    #     t = threading.Thread(target=f,args=(i['id'],))
    #     t.start()
    for i in req.json():
        t=threading.Thread(target=f,args=(i['id'],))
        t.start()