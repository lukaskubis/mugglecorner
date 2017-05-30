# controller.py

import hashlib

from os import path
from pyramid_handlers import action
from pyramid.httpexceptions import *
from functools import wraps, partial

from app.services import *


class Controller:
    def __init__(self, request):
        self.request = request


    @staticmethod
    def renderer(renderer='views/{}.html.j2'):
        def set_renderer(cls):
            for key, val in cls.__dict__.items():
                if callable(val) and not key.startswith('__'):
                    setattr(cls, key, action(renderer=renderer.format(key))(val))
            return cls
        return set_renderer


    @staticmethod
    def RESTful(cls):
        return Controller.renderer('json')(cls)


    @staticmethod
    def resource(source_method):
        def _(action):
            @wraps(action)
            def action_wrapper(self):
                request = self.request.matchdict[action.__name__]
                requested_item = source_method(request)
                if requested_item is None:
                    raise HTTPNotFound(request)
                return {action.__name__:requested_item}
            return action_wrapper
        return _


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
