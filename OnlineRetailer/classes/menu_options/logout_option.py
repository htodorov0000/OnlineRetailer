from classes.menu_classes.numbered_menu import Menu

class LogoutOption(Menu):
    def __init__(self, name, description, account, return_menu):
        self.return_menu = return_menu
        super().__init__(name, description, account)
        
    def start(self):
        self.account.log_out()
        self.return_menu.start()
