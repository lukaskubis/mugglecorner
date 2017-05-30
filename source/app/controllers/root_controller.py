# root_controller.py

from .controller import *

class RootController(Controller):

    @action(renderer='views/index.html.j2')
    def index(self):
        return {}

    @action(renderer='views/entry.html.j2')
    @Controller.resource(DataService.get_entry)
    def entry(self):
        pass
