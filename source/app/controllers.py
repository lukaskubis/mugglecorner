# controllers.py

import hashlib
from os import path
from pyramid_handlers import action


class Controller:
    def __init__(self, request):
        self.request = request

    def cache(self, static):
        if not static:
            return 'ERROR_NO_FILE:\n ({})'.format(static)

        # resolve paths to static content
        fullpath = path.dirname(path.abspath(__file__))
        fullname = path.abspath(path.join(fullpath, static.lstrip('/')))

        if not path.exists(fullname):
            return 'ERROR_MISSING_FILE:\n ({})'.format(fullname)

        # get file hash
        md5 = hashlib.md5()
        with open(fullname, 'rb') as fin:
            data = fin.read()
            md5.update(data)

        return static + '?cacheId=' + md5.hexdigest()


class HomeController(Controller):
    @action(renderer='views/index.html.j2')
    def index(self):
        return {}


class PodcastController(Controller):
    @action(renderer='views/podcast.html.j2')
    def index(self):
        return {}
