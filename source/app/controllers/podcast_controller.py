# podcast_controller.py

from .controller import *

@Controller.renderer()
class PodcastController(Controller):
    def podcast(self):
        return {}
