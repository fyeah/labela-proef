from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from sqlalchemy.exc import IntegrityError

from ..models import Product

@view_defaults(renderer='json', route_name='product_collection')
class ProductCollectionView(object):
	def __init__(self, request):
		self.request = request

	@view_config(request_method='GET')
	def get_all(self):
		request = self.request
		return request.dbsession.query(Product).all()


	@view_config(request_method='POST')
	def create(self):
		try:
			request = self.request;
			product = Product(**request.json_body)
			
			request.dbsession.add(product)
			request.dbsession.flush()
			request.response.status = 201
			return product
		except IntegrityError as error:
			print(error)
			request.response.status = 400
			return {'message' : 'Invalid parameters'}


@view_defaults(renderer='json', route_name='product')
class ProductView(object):
	def __init__(self, request):
		self.request = request
		product_id = int(request.matchdict['id'])
		self.product = request.dbsession.query(Product).get(product_id)

	@view_config(request_method='GET')
	def get_by_id(self):
		product = self.product
		if product is not None:	
			return product
		else:
			request.response.status = 404
			return {'message' : 'Product not found'}

	# add put/delete
