"""
"""

from datetime import timedelta

from wheezy.http import CacheProfile

from config import config


static_cache_profile = CacheProfile(
    'public',
    duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'],
    namespace='static',
    enabled=config.getboolean('cache-profile', 'static-enabled'))
public_cache_profile = CacheProfile(
    'server',
    duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'],
    vary_cookies=['_a'],
    no_store=True,
    enabled=config.getboolean('cache-profile', 'public-enabled'))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: