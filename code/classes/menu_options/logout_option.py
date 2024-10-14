"""This module houses the LogoutOption class."""
from classes.menu_classes.numbered_menu import Menu

class LogoutOption(Menu):
    """Selectable option to log out the user."""
    def __init__(self, name, description, account, return_menu):
        self.return_menu = return_menu
        super().__init__(name, description, account)

    def start(self):
        """Menu is drawn when this is called. Requests the user
        to be logged out from the AccountManager."""
        self.account.log_out()
        self.return_menu.start()
