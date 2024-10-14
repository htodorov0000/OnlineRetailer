"""This module houses the UserListMenu class."""
from classes.menu_classes.numbered_menu import NavigationMenu

class UserListMenu(NavigationMenu):
    """Admin only menu which shows list of users."""
    def __init__(self, name, description, account, database, landing):
        self.database = database
        self.landing = landing
        super().__init__(name, description, account)

    def start(self):
        """Called to begin drawing menu."""
        self.options = self.database.get_user_list(self.account, self.landing)
        super().start()
