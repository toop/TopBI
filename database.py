#!/usr/bin/env python
#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine('postgresql://admin:admin@localhost/topbi',echo = True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db_engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import *
    Base.metadata.create_all(bind=engine)
'''
#考虑增加用户数据选择
# mysql
mysql_db = create_engine('mysql://scott:tiger@localhost/topbi')

# oracle
oracle_db = create_engine('oracle://scott:tiger@127.0.0.1:1521/topbi')

# oracle via TNS name
oracle_db = create_engine('oracle://scott:tiger@topbi')

# mssql using ODBC datasource names.  PyODBC is the default driver.
mssql_db = create_engine('mssql://topbi')
mssql_db = create_engine('mssql://scott:tiger@topbi')

# firebird
firebird_db = create_engine('firebird://scott:tiger@localhost/topbi.gdm')
'''