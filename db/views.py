from django.shortcuts import *

def utf8(param):
    if param is None or isinstance(param, str):
        return param
    return param.encode('utf-8')

# Create your views here.
