#!/usr/bin/env python

import os

#try:
from setuptools import setup
#except:
#    from distutils.core import setup  # noqa

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

install_requires = [
    'wheezy.core>=0.1.101',
    'wheezy.caching>=0.1.83',
    'wheezy.html>=0.1.125',
    'wheezy.http>=0.1.262',
    'wheezy.routing>=0.1.145',
    'wheezy.security>=0.1.46',
    'wheezy.template>=0.1.132',
    'wheezy.validation>=0.1.84',
    'wheezy.web>=0.1.340',
]

install_optional = [
    'pylibmc>=1.2.3',
    #'PIL>=1.1.7',
    'lxml>=2.3.6',
    'pycrypto>=2.6',
]

install_requires += install_optional

try:
    import uuid  # noqa
except ImportError:
    install_requires.append('uuid')

dependency_links = [
    # pylibmc
    'https://bitbucket.org/akorn/wheezy.caching/downloads',
    # PIL
    #'https://bitbucket.org/akorn/wheezy.captcha/downloads',
    # lxml
    'https://bitbucket.org/akorn/wheezy.http/downloads',
    # pycrypto
    'https://bitbucket.org/akorn/wheezy.security/downloads'
]

setup(
    name='mysite',
    version='0.1',
    description='MySite Project',
    long_description=README,
    url='https://scm.dev.local/svn/mysite/trunk',

    author='MySite Team',
    author_email='mysite at dev.local',

    license='COMMERCIAL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        'public',
    ],
    package_dir={'': 'src'},

    zip_safe=False,
    install_requires=install_requires,
    dependency_links=dependency_links,
    extras_require={
    },

    platforms='any'
)
