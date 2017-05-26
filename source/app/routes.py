# routes.py

from .controllers import *

def add_controller_routes(url, ctrl, name, action, *, enable_id=True, root_action=False, name_action=False):
    kwargs = dict(handler=ctrl, action=action)

    # 'index' gets always assigned as root to the name
    if action=='index':
        url(name + '_ctrl_index', '/' + name, **kwargs)
        url(name + '_ctrl_index/', '/' + name + '/', **kwargs)
        if enable_id:
            url(name + '_ctrl_index_id', '/' + name + '/{id}', **kwargs)
            url(name + '_ctrl_index_id/', '/' + name + '/{id}/', **kwargs)
        return

    # name not required in url
    if root_action:
        url(name + '_ctrl_root' + action, '/' + action, **kwargs)
        url(name + '_ctrl_root/' + action, '/' + action + '/', **kwargs)
        if enable_id:
            url(name + '_ctrl_root_id' + action, '/' + action + '/{id}', **kwargs)
            url(name + '_ctrl_root_id/' + action, '/' + action + '/{id}/', **kwargs)

    # full url version
    if name_action:
        url(name + '_ctrl_' + action, name + '/' + action, **kwargs)
        url(name + '_ctrl/' + action + '/', name + '/' + action + '/', **kwargs)
        if enable_id:
            url(name + '_ctrl_id' + action, name + '/' + action + '/{id}', **kwargs)
            url(name + '_ctrl_id/' + action, name + '/' + action + '/{id}/', **kwargs)


def init_routes(config):
    url = config.add_handler
    # static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    # defaults
    url('root', '/', handler=RootController, action='index')

    # podcast views
    add_controller_routes(url, PodcastController, 'podcast', 'index')
    add_controller_routes(url, PodcastController, 'podcast', 'episode', name_action=True)
    add_controller_routes(url, PodcastController, 'podcast', 'episodes', name_action=True)
