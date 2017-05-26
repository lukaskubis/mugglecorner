# routes.py

from .controllers import *

def init_routes(config):

    # static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    # defaults
    config.add_handler('root', '/', handler=RootController, action='index')
    config.add_handler('podcast', '/podcast', handler=PodcastController, action='index')
