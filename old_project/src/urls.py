"""
"""

from wheezy.routing import url

from public.web.urls import error_urls
from public.web.urls import public_urls
from public.web.urls import static_urls
from public.web.views import WelcomeHandler

## project
from views.test import test
from views.list import ListHandler

all_urls = [
    url('', WelcomeHandler, name='default'),
    url('', ListHandler, name='default'),
    url('add', ListHandler, name='list')

]
all_urls += public_urls
all_urls += [('error/', error_urls)]
all_urls += static_urls

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: