from classes.menu import Menu

class SecurityMenuOption(Menu):
    def __init__(self, name, description, account, security_manager, selection):
        self.selection = selection
        self.security_manager = security_manager
        super().__init__(name, description, account)

    def start(self):
        self.security_manager.security = self.selection
        print(self.description)