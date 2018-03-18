from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Numeric
)

from .meta import Base


class Product(Base):
	__tablename__ = 'product'
	id = Column(Integer, primary_key=True)
	name = Column(Text, nullable=False, unique=True)
	description = Column(Text, nullable=False)
	price = Column(Numeric(precision=7, scale=2), nullable=False)
