from config import engine, Session
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CandidateRawData(Base):
    __tablename__ = 'candidate_raw_data'  
    candidate_id = Column(Integer, primary_key=True) 
    raw_data = Column(String)



