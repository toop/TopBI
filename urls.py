# -*- coding: UTF-8 -*-

## wheezy
from wheezy.routing import url
from wheezy.web.handlers import file_handler
from wheezy.web.handlers import BaseHandler
from wheezy.http import HTTPResponse

## project
from views.test import test
from views.list import ListHandler

all_urls = [
    url('', ListHandler, name='default'),
    url('welcome',test,name='default'),
    url('add', ListHandler, name='list'),
    url('static/{path:any}',
        file_handler(root='static/'),
        name='static')
]


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
