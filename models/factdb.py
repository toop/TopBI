# -*- coding: UTF-8 -*-
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class olap_fact_database(Base):
    __tablename__ = 'olap.fact.database'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False,unique=True)
    db_name = Column(String(50),nullable=False,unique=True)
    db_login = Column(String(50),nullable=False)
    db_password = Column(String(50),nullable=False) 
    db_host = Column(String(64),nullable=False)
    db_port = Column(Integer,nullable=False)
    # db_type = ([('mysql','MySQL' ),('postgres','PostgreSQL' ),('oracle','Oracle' )],'Database type',nullable=False),
    #con_url =  Column.function(_connection_get,method = True,type = 'char',string = 'Connection URL',size = 128 )
    #table_ids = one2many('olap.database.tables','fact_database_id','Tables' )
    loaded = Column(Boolean)


    def __init__(self, name, db_name, db_login, db_password, db_host, db_port, db_type, con_url, table_ids, loaded):
        self.name = name
        self.db_name = db_name
        self.db_login = db_login
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_type = db_type
        self.con_url = con_url
        self.table_ids = table_ids
        self.loaded = loaded

    def __repr__(self):
        return "<olap_fact_database('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.name,
												    self.db_name,
												    self.db_login,
												    self.db_password,
												    self.db_host,
												    self.db_port,
												    self.db_type,
												    self.con_url,
												    self.table_ids,
												    self.loaded
												    )
