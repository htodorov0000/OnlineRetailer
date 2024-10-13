"""Houses the SecurityMenuOption class."""
from classes.menu_classes.menu import Menu

class SecurityMenuOption(Menu):
    """Class for the Security ON/OFF menu option."""
    def __init__(self, name, description, account, security_manager, selection):
        self.selection = selection
        self.security_manager = security_manager
        super().__init__(name, description, account)

    def start(self):
        """Called when menu is to be drawn, requests
        setting of security mode by SecurityManager."""
        self.security_manager.set_security_mode(self.selection)
        print(self.description)
