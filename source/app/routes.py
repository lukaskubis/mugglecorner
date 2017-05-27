# routes.py

from .controllers import *


def init_routes(config):
    # static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    # podcast routes
    podcast = PodcastController, 'index'
    config.add_handler('f_podcast_episodes_id_', 'podcast/episodes/{id}/', *podcast)
    config.add_handler('f_podcast_episodes_id', 'podcast/episodes/{id}', *podcast)
    config.add_handler('f_podcast_episode_id_', 'podcast/episode/{id}/', *podcast)
    config.add_handler('f_podcast_episode_id', 'podcast/episode/{id}', *podcast)
    config.add_handler('f_podcast_episodes_', 'podcast/episodes/', *podcast)
    config.add_handler('f_podcast_episodes', 'podcast/episodes', *podcast)
    config.add_handler('f_podcast_id_', 'podcast/{id}/', *podcast)
    config.add_handler('f_podcast_id', 'podcast/{id}', *podcast)
    config.add_handler('f_podcast_', 'podcast/', *podcast)
    config.add_handler('f_podcast', 'podcast', *podcast)


    # defaults/entry routes
    defaults = RootController, 'entry'
    config.add_handler('r_entry_id_', '/entry/{id}/', *defaults)
    config.add_handler('r_entry_id', '/entry/{id}', *defaults)
    config.add_handler('r_id_', '/{id}/', *defaults)
    config.add_handler('r_id', '/{id}', *defaults)
    config.add_handler('r', '/', RootController, 'index')
