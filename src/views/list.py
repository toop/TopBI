#encoding=utf-8
""" ``views`` module.
"""

## wheezy
from wheezy.http import HTTPResponse
from wheezy.http import HTTPRequest
from wheezy.web.handlers import BaseHandler

## project 
#from config import cached
#from database import db_session


#from models import Greeting
#from repository import Repository
#from validation import greeting_validator
response = HTTPResponse()





class ListHandler(BaseHandler):
    def get(self):
        name = 'world'
        response = self.render_response('list.html',name = name)
        return response
    def list(self):
        name = 'list.'
        response = self.render_response('list.html', name = name)
        return response

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
