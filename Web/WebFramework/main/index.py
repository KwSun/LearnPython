#!/usr/bin/env python
#coding:utf-8

from wsgiref.simple_server import make_server
import conf

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #1、获取用户的URL
    userUrl = environ['PATH_INFO']
    #根据URL返回不同结果
    func = None
    for item in conf.url:
        if item[0] == userUrl:
            func = item[1]
            break
    if func:
        result = func()
    else:
        result = '404'
    
    return result

    

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()