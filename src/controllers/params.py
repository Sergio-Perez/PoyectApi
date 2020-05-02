from flask import request
from src.app import app

def params(fn):
    def wrapper():
        kwargs = request.args
        return fn(**kwargs) 
    wrapper.__name__ = fn.__name__

    return wrapper