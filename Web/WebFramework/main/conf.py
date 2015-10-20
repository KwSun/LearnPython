#!/usr/bin/env python
#coding:utf-8


def index():
    return 'index'

def login():
    return 'login'

url = (
       ('/index/',index),
       ('/login/',login),
)