"""Houses classes of menu options found in the
Admin-only user list."""

from classes.menu_classes.menu import Menu
from classes.menu_classes.numbered_menu import NavigationMenu

class UserListOption(NavigationMenu):
    """Class for menu option of selected user."""
    def __init__(self, name, description, account, landing, database):
        description = "Choose what to do with this user: " + name
        user_delete = UserDeleteOption("Delete Account", "desc", account, landing, database, name)
        user_promote = UserPromoteOption("Promote Account To Admin", "desc", account, landing, database,name)
        user_demote = UserDemoteOption("Demote Account From Admin", "desc", account, landing, database,name)
        if database.is_user_admin(name):
            name += " (ADMIN)"
        self.options = [user_delete, user_promote, user_demote, landing]
        super().__init__(name, description, account)

class UserDeleteOption(Menu):
    """Class for menu option which deletes selected user."""
    def __init__(self, name, description, account, return_menu, database, username):
        self.return_menu = return_menu
        self.username = username
        self.database = database
        super().__init__(name, description, account)

    def start(self):
        """Called when menu is to be drawn, requests deletion of 
        selected user from database."""
        self.database.delete_user(self.username)
        self.return_menu.start()

class UserPromoteOption(Menu):
    """Class for menu option which promotes selected user to admin."""
    def __init__(self, name, description, account, return_menu, database, username):
        self.return_menu = return_menu
        self.username = username
        self.database = database
        super().__init__(name, description, account)

    def start(self):
        """Called when menu is to be drawn, requests
        promotion of selected user to admin."""
        self.database.promote_to_admin(self.username)
        print("User promoted to admin.")
        self.return_menu.start()

class UserDemoteOption(Menu):
    """Class for menu option which demotes selected admin to user."""
    def __init__(self, name, description, account, return_menu, database, username):
        self.return_menu = return_menu
        self.username = username
        self.database = database
        super().__init__(name, description, account)

    def start(self):
        """Called when menu is to be drawn, requests
        demotion of selected admin to user."""
        self.database.demote_from_admin(self.username)
        print("User demoted from admin.")
        self.return_menu.start()
