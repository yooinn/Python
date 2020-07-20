from .app_test import app
import requests
@app.task
def add(x,y):
    return y**x
