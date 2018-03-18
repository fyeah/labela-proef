from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import joinedload

from ..models import User


@view_defaults(renderer='json', route_name='user_collection')
class UserCollectionView(object):
	def __init__(self, request):
		self.request = request

	@view_config(request_method='GET')
	def get_all(self):
		request = self.request
		return request.dbsession.query(User).all()


	@view_config(request_method='POST')
	def create(self):
		try:
			request = self.request;
			user_data = request.json_body
			pw = user_data['password']
			del user_data['password']

			user = User(**user_data)
			user.set_password(pw)
			
			request.dbsession.add(user)
			request.dbsession.flush()
			request.response.status = 201
			return user
		except IntegrityError as error:
			# Distinguish between invalid body (400)
			# and email already exists (409)
			print(error)
			request.response.status = 400	
			return {'message' : 'Invalid data'}


# add GET, PUT, DELETE for /users/{id}
