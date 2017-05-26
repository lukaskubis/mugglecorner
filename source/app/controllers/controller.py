# controller.py

import hashlib
from os import path
from pyramid_handlers import action
from functools import wraps


class Controller:
    def __init__(self, request):
        self.request = request

    @staticmethod
    def renderer(renderer):
        def set_renderer(cls):
            for key, val in cls.__dict__.items():
                if callable(val):
                    setattr(cls, key, action(renderer=renderer)(val))
            return cls
        return set_renderer

    @staticmethod
    def RESTful(cls):
        return Controller.renderer('json')(cls)

    @staticmethod
    def index(action):
        @wraps(action)
        def wrapper(self):
            return self.index()
        return wrapper

    @staticmethod
    def url_id_check(func):
        def redirect_to_view(action):
            @wraps(action)
            def redirect(self):
                _action = action
                params = self.request.matchdict
                if 'id' in params:
                    try:
                        _ = func(params['id'])
                    except Exception:
                        cls_dict = self.__class__.__dict__
                        methods = [k for k, v in cls_dict.items() if callable(v)]
                        if params['id'] in methods:
                            self.request.matchdict = {}
                            _action = cls_dict[params['id']]
                return _action(self)
            return redirect
        return redirect_to_view

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
