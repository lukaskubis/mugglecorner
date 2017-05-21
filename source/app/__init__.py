# __init__.py

import os
from pyramid.config import Configurator
from .data import init_db


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('social_pyramid')

    # initialize the database here
    init_db(os.path.dirname(__file__))

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
