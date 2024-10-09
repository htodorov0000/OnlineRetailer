from classes.menu_classes.menu import Menu
from classes.menu_classes.numbered_menu import NavigationMenu

class UserListOption(NavigationMenu):
    def __init__(self, name, description, account, landing, database):
        description = "Choose what to do with this user: " + name
        user_delete = UserDeleteOption("Delete Account", "desc", account, self, database, name)
        user_promote = UserPromoteOption("Promote Account To Admin", "desc", account, self, database,name)
        user_demote = UserDemoteOption("Demote Account From Admin", "desc", account, self, database,name)
        if database.is_user_admin(name):
            name += " (ADMIN)"
        self.options = [user_delete, user_promote, user_demote, landing]
        super().__init__(name, description, account)
        
class UserDeleteOption(Menu):
    def __init__(self, name, description, account, return_menu, database, username):
        self.return_menu = return_menu
        self.username = username
        self.database = database
        super().__init__(name, description, account)
    
    def start(self):
        pass #Delete
    
class UserPromoteOption(Menu):
    def __init__(self, name, description, account, return_menu, database, username):
        self.return_menu = return_menu
        self.username = username
        self.database = database
        super().__init__(name, description, account)
    
    def start(self):
        self.database.promote_to_admin(self.username)
        print("User promoted to admin.")
        self.return_menu.start()
        
class UserDemoteOption(Menu):
    def __init__(self, name, description, account, return_menu, database, username):
        self.return_menu = return_menu
        self.username = username
        self.database = database
        super().__init__(name, description, account)
    
    def start(self):
        self.database.demote_from_admin(self.username)
        print("User demoted from admin.")
        self.return_menu.start()
        
