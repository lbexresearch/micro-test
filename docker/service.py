import hug
import sys
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

@hug.get('/sleep', examples='sec=2',versions=[1,2])
@hug.local()
def sleep(sec: hug.types.float_number):
    time.sleep(sec)
    return {'sleep': True, 'took': sec}

@hug.get('/', versions=1)
def root():
    return {'micro-test': "0.0.1", 'took': 0}

@hug.get('/uptime', versions=1)
@hug.local()
def uptime():
    return {'uptime': time.time() - starttime, 'took': 0}

@hug.get('/uptime', versions=2)
@hug.local()
def uptime():
    t=randint(0,9) 
    time.sleep(t/10)
    return {'uptime': time.time() - starttime, 'took': t/10}

@hug.get('/platform', versions=[1,2])
@hug.local()
def platform():
    return {'platform': platform.platform(), 'took': 0}

@hug.get('/version')
@hug.local()
def version():
    return {'version': 3.5, 'took': 0}

@hug.get('/crash', versions=[1,2])
@hug.local()
def platform():
    sys.exit(1)
    return {'crash': "Now", 'took': 0}

