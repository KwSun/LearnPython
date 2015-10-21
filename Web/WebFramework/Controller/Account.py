#!/usr/bin/env python
#coding:utf-8

def Login():
    #读取页面文件 
    #数据库比较 Model
    #返回用户信息 View
    f = file('/Users/apple/Documents/workspace/WebFramework/View/login.html')
    data = f.read()
    return data

def Logout():
    return 'login'

