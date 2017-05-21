# __init__.py

from pyramid.config import Configurator
from .data import db_init


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('social_pyramid')

    # custom jinja2 extension
    config.add_jinja2_renderer('.j2')

    # initialize the database
    db_init()

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
