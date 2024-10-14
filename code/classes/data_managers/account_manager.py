"""This module houses the AccountManager class"""
class AccountManager:
    """Tracks whether the user is logged in or out, as well as if they have admin privileges."""
    def __init__(self):
        self.logged_in = False
        self.username = ""
        self.admin = False
        self.menu_object_manager = None

    def set_menu_object_manager(self, menu_object_manager):
        """For accessing menu_object_manager later."""
        self.menu_object_manager = menu_object_manager

    def login(self, username, admin):
        """Sets the user to logged in, sets the username they are logged under
       and if they have admin privileges, so these variables can be accessed later."""
        self.username = username
        if admin == "TRUE":
            self.admin = True
        elif admin == "FALSE":
            self.admin = False
        self.logged_in = True
        if self.admin:
            self.menu_object_manager.admin_menu_options()
        else:
            self.menu_object_manager.user_menu_options()

    def log_out(self):
        """Logs the user out, blanks out username and admin access."""
        self.username = ""
        self.admin = False
        self.logged_in = False
        self.menu_object_manager.guest_menu_options()
    