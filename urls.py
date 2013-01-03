""" ``urls`` module.
"""

from wheezy.routing import url
from wheezy.web.handlers import file_handler

from views import list


all_urls = [
    url('', list, name='list'),
    url('static/{path:any}',
        file_handler(root='static/'),
        name='static')
]
