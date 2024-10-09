from classes.menu_classes.numbered_menu import NavigationMenu

class UserListMenu(NavigationMenu):
    
    def __init__(self, name, description, account, database, landing):
        self.database = database
        self.landing = landing
        super().__init__(name, description, account)

    def start(self):
        self.options = self.database.get_user_list(self.account, self.landing)
        super().start()
