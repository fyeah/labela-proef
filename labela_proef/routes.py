def includeme(config):
	config.add_route('home', '/')

	config.add_route('product_collection', '/products');
	config.add_route('product', '/products/{id}');

	config.add_route('user_collection', '/users');

	config.add_route('order_collection', '/orders');
	config.add_route('order', '/orders/{id}');


