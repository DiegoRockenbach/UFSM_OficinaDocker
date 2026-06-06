import time

import redis
from flask import Flask, url_for

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

BASE_SIZE = 150
GROWTH_RATE = 1.3

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    img_size = int(BASE_SIZE * (GROWTH_RATE ** (count - 1)))
    img_url = url_for('static', filename='silvera.jpeg')
    html = (
        '<style>'
        'body {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }}'
        '</style>'
        '<h1>Olá mundo!</h1>'
        '<h2>Você já abriu essa página {} vezes.</h2>'
        '<img src="{}" width="{}" height="{}" alt="logo">'
    ).format(count, img_url, img_size, img_size)
    return html
