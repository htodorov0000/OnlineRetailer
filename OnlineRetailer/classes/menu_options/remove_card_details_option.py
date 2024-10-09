from classes.menu_classes.menu import Menu

class RemoveCardDetailsOption(Menu):
    def __init__(self, name, description, account, database, return_menu):
        self.database = database
        self.return_menu = return_menu
        super().__init__(name, description, account)

    def start(self):
        self.database.remove_card_details(self.account)
        print("Card details removed successfully.")
        self.return_menu.start()