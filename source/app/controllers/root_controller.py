# root_controller.py

from .controller import *

@Controller.renderer()
class RootController(Controller):
    def index(self):
        return {}

    @Controller.resource(DataService.get_entry)
    def entry(self):
        pass
