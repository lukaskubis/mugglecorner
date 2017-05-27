# routes.py

from .controllers import *

def set_urls(config, route_id, url, enable_id=True, **kwargs):
    config.add_handler(f'{route_id}', url, **kwargs)
    config.add_handler(f'{route_id}/', url + '/', **kwargs)
    if enable_id:
        config.add_handler(f'{route_id}_id', url + '/{id}', **kwargs)
        config.add_handler(f'{route_id}_id_', url + '/{id}/', **kwargs)


def add_controller_routes(config, ctrl, action, *, enable_id=True, root_action=False, name_action=True):
    kwargs = dict(handler=ctrl, action=action)
    urlname = ctrl.__urlname__
    route = f'_{urlname}_{action}'

    if action=='index':
        return set_urls(config, f'i{route}', f'/{urlname}', enable_id, **kwargs)
    if root_action:
        set_urls(config, f'r{route}', f'/{action}', enable_id, **kwargs)
    if name_action:
        set_urls(config, f'f{route}', f'{urlname}/{action}', enable_id, **kwargs)


def init_routes(config):
    set_url = config.add_handler
    # static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    # defaults
    set_url('root', '/', handler=RootController, action='index')

    # podcast views
    add_controller_routes(config, PodcastController, 'index')
    add_controller_routes(config, PodcastController, 'episode')
    add_controller_routes(config, PodcastController, 'episodes')
