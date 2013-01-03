from sqlalchemy import Column, Integer, String
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
	created_on = Column(String)

    def __init__(self, name, fullname, password,created_on=None):
        self.name = name
        self.fullname = fullname
        self.password = password
		self.created_on = created_on or datetime.now()

    def __repr__(self):
       return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)