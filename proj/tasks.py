from datetime import datetime

from .app_test import app
import requests
@app.task
def add(x,y):
    return y**x
@app.task
def time_teller():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")