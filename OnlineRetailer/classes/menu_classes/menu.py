"""This module houses the Menu class."""
class Menu:
    """Base Menu class which other Menu classes extend."""
    def __init__(self, name, description, account):
        self.name = name
        self.description = description
        self.account = account

    def start(self):
        """Function called when starting a menu."""
        self.draw_menu()

    def draw_name_and_description(self):
        """Prints name and description of menu."""        
        print()
        if self.account.logged_in:
            print("                                                 User:", self.account.username)
        else:
            print("                                                 Guest")
        if self.account.admin:
            print("                                                 (Admin Account)")
        print()
        print("***" + self.name.upper() + "***")
        print()
        if self.description != "": #Print description if it isn't empty.
            print(self.description)
            print()

    def draw_menu(self):
        """Draws menu. Used for classes extending this one."""
        self.draw_name_and_description()
