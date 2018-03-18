from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	Numeric,
	DateTime,
	Enum,
	ForeignKey
)
from sqlalchemy.orm import relationship

import enum
import datetime


from .meta import Base
from .order_line import OrderLine

class StatusEnum(enum.Enum):
	CREATED = 'CREATED'
	PAYMENT_RECEIVED = 'PAYMENT_RECEIVED'
	SENT = 'SENT'
	DELIVERED = 'DELIVERED'


class Order(Base):
	__tablename__ = 'order'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	total_price = Column(Numeric(precision=12, scale=2), nullable=False)
	created_at = Column(DateTime, nullable=False, default=datetime.now())
	preferred_delivery_moment = Column(DateTime(timezone=False))
	status = Column(Enum(StatusEnum), nullable=False)
	order_lines = relationship(OrderLine)
