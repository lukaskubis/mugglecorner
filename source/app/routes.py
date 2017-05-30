# routes.py

from .controllers import *


def init_routes(config):
    # static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    # podcast routes
    podcast_episode = PodcastController, 'episode'
    config.add_handler('f_podcast_id_', 'podcast/{episode}/', *podcast_episode)
    config.add_handler('f_podcast_id', 'podcast/{episode}', *podcast_episode)

    podcast = PodcastController, 'podcast'
    config.add_handler('f_podcast_', 'podcast/', *podcast)
    config.add_handler('f_podcast', 'podcast', *podcast)

    # entry routes
    entry = RootController, 'entry'
    config.add_handler('r_entry_id_', '/entry/{entry}/', *entry)
    config.add_handler('r_entry_id', '/entry/{entry}', *entry)

    # access entries from root path
    config.add_handler('r_id_', '/{entry}/', *entry)
    config.add_handler('r_id', '/{entry}', *entry)

    # root
    defaults = RootController, 'index'
    config.add_handler('r', '/', *defaults)
