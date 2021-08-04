from pymemcache.client import base
from flask import Flask, request
import os

app = Flask(__name__)
memcache_client = base.Client(("localhost", 11211))


@app.route('/<k>')
def get_fibo_num(k):
    fibo = memcache_client.get(k)
    fibo = None
    if fibo is None:
        fibo = count_fibo_num(int(k))        
        memcache_client.set(k, fibo)
    return int(fibo), 200

def count_fibo_num(k):
    fibo, fibo_next = 0, 1
    for _ in range(k - 1):
        fibo, fibo_next = fibo_next, fibo + fibo_next
    return fibo
