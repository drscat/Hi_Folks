#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Summary, Counter, Gauge, Histogram
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

# Counter

c = Counter('my_failures', 'Description of counter')
c.inc()     # Increment by 1
c.inc(1.6)  # Increment by given value

@c.count_exceptions()
def f():
  pass

with c.count_exceptions():
  pass

# Count only one type of exception
with c.count_exceptions(ValueError):
  pass

# Counter

# Gauge

g = Gauge('my_inprogress_requests', 'Description of gauge')
g.inc()      # Increment by 1
g.dec(10)    # Decrement by given value
g.set(4.2)   # Set to a given value

g.set_to_current_time()   # Set to current unixtime

# Increment when entered, decrement when exited.
@g.track_inprogress()
def f():
  pass

with g.track_inprogress():
  pass

# Gauge

# Histogram

from prometheus_client import Histogram
h = Histogram('request_latency_seconds', 'Description of histogram')
h.observe(4.7)    # Observe 4.7 (seconds in this case)

@h.time()
def f():
  pass

with h.time():
  pass

# Histogram


app = Flask(__name__)

@app.route("/metrics")
def metrics_fun():
    return app_dispatch

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

@app.route("/")
def hi_fun():
    return "Hi Folks\n"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
