from classes.numbered_menu import NavigationMenu

class LogoutOption(NavigationMenu):
    def __init__(self, name, description, account, landing):
        self.landing = landing
        super().__init__(name, description, account)
        
    def start(self):
        self.account.log_out()
        self.landing.start()
