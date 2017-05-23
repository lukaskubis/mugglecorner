# __init__.py

from pyramid.config import Configurator
from .data import init_db
from .routes import init_routes


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_handlers')

    # custom jinja2 extension
    config.add_jinja2_renderer('.j2')

    # initialize the database and routes
    init_db()
    init_routes(config)

    config.scan()
    return config.make_wsgi_app()
