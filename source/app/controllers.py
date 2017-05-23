# controllers.py

from pyramid_handlers import action


class Controller:
    def __init__(self, request):
        self.request = request


class HomeController(Controller):
    @action(renderer='views/index.html.j2')
    def index(self):
        return {}


class PodcastController(Controller):
    @action(renderer='views/podcast.html.j2')
    def index(self):
        return {}
