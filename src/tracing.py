
"""
"""

import os
import platform
import socket
import sys

from datetime import timedelta
from time import time


start_time = time()


def error_report_extra_provider(request):
    ts = os.times()
    e = request.environ
    if 'CONTENT_LENGTH' in e and e['CONTENT_LENGTH']:
        form = filter_names(request.form, ignore=(
            'password',
            'confirm_password'
        ))
    else:
        form = {}
    return {
        'HTTP_ACCEPT_LANGUAGE': e['HTTP_ACCEPT_LANGUAGE'],
        'HTTP_REFERER': e.get('HTTP_REFERER', '?'),
        'HTTP_USER_AGENT': e['HTTP_USER_AGENT'],
        'PATH_INFO': e['PATH_INFO'],
        'REMOTE_ADDR': e['REMOTE_ADDR'],
        'REQUEST_METHOD': e['REQUEST_METHOD'],
        'executable': sys.executable,
        'hostname': socket.gethostname(),
        'http_cookies': request.cookies,
        'http_form': form,
        'machine': platform.machine(),
        'modules': modules_info(),
        'process_uptime': timedelta(seconds=time() - start_time),
        'python_compiler': platform.python_compiler(),
        'python_version': platform.python_version(),
        'release': platform.release(),
        'route_args': dict(e['route_args']),
        'stime': timedelta(seconds=ts[1]),
        'system': platform.system(),
        'utime': timedelta(seconds=ts[0]),
        'uwsgi.version': e.get('uwsgi.version', '?'),
    }


def filter_names(d, ignore):
    return dict((name, d[name]) for name in d if name not in ignore)


def modules_info():
    def predicate(m):
        return (hasattr(m, '__version__')
                and not (m.__name__.startswith('_') or '._' in m.__name__))
    return sorted([(m.__name__, m.__version__) for m in sys.modules.values()
                   if predicate(m)])


ERROR_REPORT_FORMAT = """
%(message)s

Environ Variables
-----------------
PATH_INFO: %(PATH_INFO)s
REQUEST_METHOD: %(REQUEST_METHOD)s
REMOTE_ADDR: %(REMOTE_ADDR)s
HTTP_REFERER: %(HTTP_REFERER)s
HTTP_ACCEPT_LANGUAGE: %(HTTP_ACCEPT_LANGUAGE)s
HTTP_USER_AGENT: %(HTTP_USER_AGENT)s

HTTP Request
------------
Route: %(route_args)s
Cookies: %(http_cookies)s
Form: %(http_form)s

Hosting Process
---------------
Process Id: %(process)d
Up Time: %(process_uptime)s
User Time: %(utime)s
System Time: %(stime)s

Machine Platform
----------------
Host: %(hostname)s
OS: %(system)s %(release)s %(machine)s
Python Version: %(python_version)s [%(python_compiler)s]
uWSGI Version: %(uwsgi.version)s
Executable: %(executable)s
Timestamp: %(asctime)s

Loaded Modules
--------------
%(modules)s


"""
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: