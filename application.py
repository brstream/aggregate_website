import os

from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

here = os.path.dirname(os.path.abspath(__file__))

def main():
    # configuration settings
    settings = {}
    settings['db'] = os.path.join(here, 'data.db')
    settings['mako.directories'] = os.path.join(here, 'templates')
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    # configuration setup
    config = Configurator(settings=settings)
    config.scan("views")
    config.scan("subscribers")
    # routes setup
    config.add_route('list', '/')
    # serve app
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
