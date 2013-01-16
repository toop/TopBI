#encoding=utf-8
""" ``views`` module.
"""

## wheezy
from wheezy.http import HTTPResponse
from wheezy.web.handlers import BaseHandler


class test(BaseHandler):
	def get(self):
		response = HTTPResponse()
		response.write('Hello,World~~get')
		return response



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
