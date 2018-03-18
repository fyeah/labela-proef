from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Numeric,
	DateTime
	ForeignKey
)

import datetime

# from sqlalchemy.orm import relationship

from .meta import Base


class OrderLine(Base):
	__tablename__ = 'order_line'
	id = Column(Integer, primary_key=True)
	order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
	product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
	price = Column(Numeric(precision=7, scale=2), nullable=False)
	amount = Column(Integer, nullable=False)
	total_price = Column(Numeric(precision=11, scale=2), nullable=False)

