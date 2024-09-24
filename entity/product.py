from sqlalchemy import BigInteger, Column, String, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base =declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(BigInteger, primary_key=True)
    code = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    value = Column(Numeric, nullable=False)
    category_id = Column(BigInteger, ForeignKey('categories_id'), nullable=False)
    category = relationship('Category', back_populates='products')
