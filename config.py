#!/usr/bin/env python
#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from wheezy.caching.memory import MemoryCache
from wheezy.caching.patterns import Cached
from wheezy.html.ext.mako import widget_preprocessor
from wheezy.web.templates import MakoTemplate

db_engine = create_engine('postgresql://admin:admin@localhost/topbi',echo = True)
Session = sessionmaker(bind=db_engine)
con = db_engine.connect()

cache = MemoryCache()
cached = Cached(cache, time=15 * 60)

options = {
    'render_template': MakoTemplate(
        directories=['templates'],
        filesystem_checks=False,
        preprocessor=[widget_preprocessor]
    )
}

options.update({
    'http_cache': cache
})
