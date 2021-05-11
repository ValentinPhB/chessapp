
from chessapp.controllers.menus_c import HomeMenuController


class ApplicationController:
    """
    This is the main controller of this application.
    it orchestrates all other controllers, all sequences.
    """

    def __init__(self):
        self.controller = None

    def start(self):
        """
        This loop allows to move to the nex controller.
         It start with redirect the user to the HomeMenuController.
        """

        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()
