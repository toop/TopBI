"""
"""

from wheezy.routing import url

from public.web.views import WelcomeHandler
from public.web.views import http400
from public.web.views import http403
from public.web.views import http404
from public.web.views import http500
from public.web.views import static_file


public_urls = [
    url('home', WelcomeHandler, name='home')
]

error_urls = [
    url('400', http400, name='http400'),
    url('403', http403, name='http403'),
    url('404', http404, name='http404'),
    url('500', http500, name='http500'),
]

static_urls = [
    url('static/{path:any}', static_file, name='static'),
    url('favicon.ico', static_file, {'path': 'img/favicon.ico'})
]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: