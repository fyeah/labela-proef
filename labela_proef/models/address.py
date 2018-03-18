# from sqlalchemy import (
# 	Column,
# 	Index,
# 	Integer,
# 	Text,
# 	String,
# 	Numeric,
# 	ForeignKey
# )

# from .meta import Base


# class Address(Base):
# 	__tablename__ = 'address'
# 	id = Column(Integer, primary_key=True)
# 	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	# street = Column(Text, nullable=False)
	# house_nr = Column(Text, nullable=False)
	# postcode = Column(Text, nullable=False)
	# city = Column(Text, nullable=False)
	# country = Column(Text, nullable=False)