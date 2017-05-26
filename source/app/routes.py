# routes.py

from .controllers import *

def add_controller_routes(cfg, ctrl, name, action, *, enable_id=False, root_action=False, name_action=False):
    kwargs = dict(handler=ctrl, action=action)

    # 'index' gets always assigned as root to the name
    if action=='index':
        cfg.add_handler(name + '_ctrl_index', '/' + name, **kwargs)
        cfg.add_handler(name + '_ctrl_index/', '/' + name + '/', **kwargs)
        if enable_id:
            cfg.add_handler(name + '_ctrl_index_id', '/' + name + '/{id}', **kwargs)
            cfg.add_handler(name + '_ctrl_index_id/', '/' + name + '/{id}/', **kwargs)
        return

    # name not required in url
    if root_action:
        cfg.add_handler(name + '_ctrl_root' + action, '/' + action, **kwargs)
        cfg.add_handler(name + '_ctrl_root/' + action, '/' + action + '/', **kwargs)
        if enable_id:
            cfg.add_handler(name + '_ctrl_root_id' + action, '/' + action + '/{id}', **kwargs)
            cfg.add_handler(name + '_ctrl_root_id/' + action, '/' + action + '/{id}/', **kwargs)

    # full url version
    if name_action:
        cfg.add_handler(name + '_ctrl', name + '/{action}', **kwargs)
        cfg.add_handler(name + '_ctrl/', name + '/{action}/', **kwargs)
        if enable_id:
            cfg.add_handler(name + '_ctrl_id', name + '/{action}/{id}', **kwargs)
            cfg.add_handler(name + '_ctrl_id/', name + '/{action}/{id}/', **kwargs)


def init_routes(config):
    url = config.add_handler
    # static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    # defaults
    url('root', '/', handler=RootController, action='index')

    # podcast views
    add_controller_routes(config, PodcastController, 'podcast', 'index', enable_id=True)
    # add_controller_routes(config, PodcastController, 'podcast', 'episode', enable_id=True)
    # add_controller_routes(config, PodcastController, 'podcast', 'episodes', enable_id=True)
