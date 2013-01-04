from sqlalchemy import Column, Integer, String
from datetime import datetime
from database import Base

class Olap_cube(Base):
    __tablename__ = 'olap_cube'

    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True)
    table_id = Column(Integer, ForeignKey("olap.cube.table"), nullable=False)
    schema_id = Column(Integer, ForeignKey("olap.schema"), nullable=False)
    dimension_ids = Column(Integer, ForeignKey("olap.dimension"), nullable=False)
    measure_ids = Column(Integer, ForeignKey("olap.olap.measure"), nullable=False)
    query_log = Column(Boolean)
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return "<olap_cube('%s')>" % (self.name)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: