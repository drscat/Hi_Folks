#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Summary


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
