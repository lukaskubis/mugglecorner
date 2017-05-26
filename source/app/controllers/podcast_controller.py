# podcast_controller.py

from .controller import *

@Controller.renderer('views/podcast.html.j2')
class PodcastController(Controller):

    @Controller.url_id_check(int)
    def index(self):
        return {}

    @Controller.index
    def episode(self): pass

    @Controller.index
    def episodes(self): pass
