"""This module houses the RemoveCardDetailsOption class."""
from classes.menu_classes.menu import Menu

class RemoveCardDetailsOption(Menu):
    """Class for menu option which removes user card details."""
    def __init__(self, name, description, account, database, return_menu):
        self.database = database
        self.return_menu = return_menu
        super().__init__(name, description, account)

    def start(self):
        """Called in order to draw menu. Requests card
        detail removal from DatabaseManager."""
        self.database.remove_card_details(self.account)
        print("Card details removed successfully.")
        self.return_menu.start()
