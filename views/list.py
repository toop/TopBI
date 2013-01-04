#encoding=utf-8
""" ``views`` module.
"""

from datetime import timedelta
from wheezy.http import HTTPResponse
from wheezy.http import HTTPRequest
from wheezy.http import CacheProfile
from wheezy.http.transforms import gzip_transform
from wheezy.http import accept_method
from wheezy.web import handler_cache
from wheezy.web.handlers import BaseHandler
from wheezy.web.transforms import handler_transforms

from config import cached
from database import db_session
#from models import Greeting
#from repository import Repository
#from validation import greeting_validator

'''
class ListHandler(BaseHandler):

    @handler_cache(CacheProfile('server', duration=timedelta(minutes=15),
                                vary_environ=['HTTP_ACCEPT_ENCODING']))
    @handler_transforms(gzip_transform(compress_level=9, min_length=250))
    def get(self):
        with session() as db:
            repo = Repository(db)
            greetings = repo.list_greetings()
        response = self.render_response('list.html',
                                        greetings=greetings)
        response.dependency_key = 'd_list'
        return response


class list(BaseHandler):
	#@handler_cache(CacheProfile('server', duration=timedelta(minutes=15),
    #   vary_environ=['HTTP_ACCEPT_ENCODING']))
	#@handler_transforms(gzip_transform(compress_level=9, 
	#	min_length=250))
	
	def get(self):
		#greeting = greeting or Greeting()
		#session=Session()
		#with con as db:
		#response=HTTPResponse()
		cur = self.con.execute("SELECT * FROM users")
		return [users(id=row[0],name=row[1],fullname=row[2],password=row[3],created_on=row[4]) for row in				cur.fetchall()]
		
		return response
'''
class list(BaseHandler):
    #@handler_cache(CacheProfile('server', duration=timedelta(minutes=15),
    #vary_environ=['HTTP_ACCEPT_ENCODING']))
    #@handler_transforms(gzip_transform(compress_level=9, 
    #min_length=250))

    def get(self):
        #greeting = greeting or Greeting()
        #session=Session()
        #with con as db:
        response=HTTPResponse()
        self.render_response ('ttt.mako')
        return response

'''

@accept_method('GET')
def listt(request):
    response=HTTPResponse()
    with session() as db:
	    rs = db.execute("SELECT id, created_on, author, message FROM greeting ORDER BY id DESC LIMIT 10")
        return [Greeting(id=row[0],
			created_on=row[1],
			author=row[2],
			message=row[3]) for row in rs.fetchall()]
	return {}


#tasks = [dict(id=row[0], authore=row[1]) for row in rs.fetchall()]
class AddHandler(BaseHandler):

    @handler_cache(CacheProfile('both', duration=timedelta(hours=1),
                                vary_environ=['HTTP_ACCEPT_ENCODING']))
    @handler_transforms(gzip_transform(compress_level=9, min_length=250))
    def get(self, greeting=None):
        greeting = greeting or Greeting()
        return self.render_response('add.html', greeting=greeting)

    def post(self):
        greeting = Greeting()
        if (not self.try_update_model(greeting)
                or not self.validate(greeting, greeting_validator)):
            if self.request.ajax:
                return self.json_response({'errors': self.errors})
            return self.get(greeting)
        with session() as db:
            repo = Repository(db)
            if not repo.add_greeting(greeting):
                self.error('Sorry, can not add your greeting.')
                return self.get(greeting)
            db.commit()
        cached.dependency.delete('d_list')
        return self.see_other_for('list')
'''

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
