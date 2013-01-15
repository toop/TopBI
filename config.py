#!/usr/bin/env python
#coding=utf-8

## wheezy
from wheezy.caching.memory import MemoryCache
from wheezy.caching.patterns import Cached
from wheezy.html.ext.mako import widget_preprocessor
from wheezy.web.templates import MakoTemplate

cache = MemoryCache()
cached = Cached(cache, time=15 * 60)

options = {
    'render_template': MakoTemplate(
        directories=['templates'],
        filesystem_checks=False,
        preprocessor=[widget_preprocessor],
        input_encoding='utf-8',
        output_encoding='utf-8',
        default_filters=['decode.utf8']
    )
}

options.update({
    'http_cache': cache
})