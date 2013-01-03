#!/usr/bin/env python
#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine('postgresql://admin:admin@localhost/topbi',echo = True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    frome models import *
    Base.metadata.create_all(bind=engine)