import api.controllers.userController as userController

class Routes():
    def __init__(self):
        self._token = userController.getUser