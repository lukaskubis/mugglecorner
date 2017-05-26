# podcast_controller.py

from .controller import *

@Controller.renderer('views/podcast.html.j2')
class PodcastController(Controller):

    def index(self):
        return self.request.matchdict

    @Controller.index
    def episode(self): pass

    @Controller.index
    def episodes(self): pass
