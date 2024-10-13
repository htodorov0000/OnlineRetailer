"""Houses the NumberedMenu and NavigationMenu classes, the latter
of which extends the former. Both extend the Menu class."""
from classes.menu_classes.menu import Menu

class NumberedMenu(Menu):
    """Menu class which prints numbered options for the user
    to select using text input. To be extended from."""

    INVALID_INPUT: str = "Invalid input type. Try again."
    INVALID_RANGE: str = "Please input a number in the correct range."
    def __init__(self, name, description, account):
        self.user_input: int
        self.menu_items = []
        super().__init__(name, description, account)

    def draw_menu(self):
        """Draws the menu and asks for user input."""
        menu_string = ""
        for num, menu_item in enumerate(self.menu_items):
            menu_string += (str(num + 1) + ". " + menu_item) + """
"""
        while True:
            self.draw_name_and_description()
            try:
                self.user_input = int(input(menu_string))
                if self.user_input < len(self.menu_items) + 1 and self.user_input > 0:
                    break
                print(self.INVALID_RANGE)
                print()
            except ValueError:
                print(self.INVALID_INPUT)
                print()
        self.apply_chosen_option()

    def apply_chosen_option(self):
        """To be used to apply chosen option in classes extending this
        one."""
        pass

class NavigationMenu(NumberedMenu):
    """Class which allows navigation between menus and selection of options."""
    def __init__(self, name, description, account):
        self.options = []
        super().__init__(name, description, account)

    def start(self):
        """Called when menu needs to be drawn."""
        menu_name_array = []
        #Draws all selectable options:
        for menu in self.options:
            menu_name_array.append(menu.name)
        self.menu_items = menu_name_array
        self.draw_menu()

    def apply_chosen_option(self):
        """Starts chosen option."""
        self.options[self.user_input - 1].start()
