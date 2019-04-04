import hug
import platform
import time
from random import randint

starttime = time.time()
print("Seconds since epoch =", starttime)


@hug.get(examples='name=Timothy&age=26')
@hug.local()
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Says happy birthday to a user"""
    return {'message': 'Happy {0} Birthday {1}!'.format(age, name),
            'took': float(hug_timer)}

@hug.get('/uptime', versions=1)
def root():
    return {'uptime': time.time() - starttime, 'took': 0}

@hug.get('/uptime', versions=2)
def root():
    t=randint(0,9) 
    time.sleep(t)
    return {'uptime': time.time() - starttime, 'took': t}


@hug.get('/platform')
def root():
    return {'platform': platform.platform(), 'took': 0}
