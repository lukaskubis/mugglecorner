# root_controller.py

from .controller import *

class RootController(Controller):
    @action(renderer='views/index.html.j2')
    def index(self):
        return {}
