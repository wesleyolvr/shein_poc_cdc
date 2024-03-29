from datetime import datetime

from db.database import Base
from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class PriceHistory(Base):
    __tablename__ = 'price_history'

    id = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP, default=datetime.now())
    price = Column(Float)
    price_real_symbol = Column(String)
    price_real = Column(Float)
    price_us_symbol = Column(String)
    price_us = Column(Float)
    discount_price_real_symbol = Column(String)
    discount_price_real = Column(Float)
    discount_price_us_symbol = Column(String)
    discount_price_us = Column(Float)
    product_id = Column(Integer, ForeignKey('products.id'))

    product = relationship('Product', back_populates='price_history')
