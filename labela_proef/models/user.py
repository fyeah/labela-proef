from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
)

import bcrypt

# from sqlalchemy.orm import relationship

from .meta import Base


class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	email = Column(Text, nullable=False, unique=True)
	password_hash = Column(Text, nullable=False)
	first_name = Column(Text, nullable=False)
	last_name = Column(Text, nullable=False)
	street = Column(Text, nullable=False)
	house_nr = Column(Text, nullable=False)
	postcode = Column(Text, nullable=False)
	city = Column(Text, nullable=False)
	country = Column(Text, nullable=False)

	def set_password(self, pw):
		print(pw)
		pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
		self.password_hash = pwhash.decode('utf8')

	def check_password(self, pw):
		if self.password_hash is not None:
			expected_hash = self.password_hash.encode('utf8')
			return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
		return False


	# email validate

