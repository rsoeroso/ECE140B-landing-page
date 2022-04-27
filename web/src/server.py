from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

def get_welcome_page(req):
    return FileResponse('templates/welcome.html')

def get_home_page(req):
    return FileResponse('templates/home.html')

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  # Add route for welcome page
  config.add_route('get_welcome_page', '/')
  config.add_view(get_welcome_page, route_name='get_welcome_page')

  # Add route for home page
  config.add_route('get_home_page', '/home')

  # Directs the route to the function that can generate the view
  config.add_view(get_home_page, route_name='get_home_page')

  # Add static view
  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  # This is the overall compiled app with the given configurations
  app = config.make_wsgi_app()

  # Start serving on port 6000
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()