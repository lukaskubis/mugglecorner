# podcast_controller.py

from .controller import *

class PodcastController(Controller):
    @action(renderer='views/podcast.html.j2')
    def index(self):
        return {}
