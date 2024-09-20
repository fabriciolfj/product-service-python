from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):

    __tablename__ = 'categories'

    id = Column(BigInteger, primary_key=True)
    description = Column(String, nullable=False)