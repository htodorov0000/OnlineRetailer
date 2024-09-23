from classes.menu import Menu

class NumberedMenu(Menu):
    INVALID_INPUT: str = "Invalid input type. Try again."
    INVALID_RANGE: str = "Please input a number in the correct range."
    def __init__(self, name, description):
        self.user_input: int
        self.menu_items = []
        self.options = []
        super().__init__(name, description)

    def draw_menu(self):
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
        pass
    
class SettingBoolMenu(NumberedMenu):   
    def __init__(self, name, description):
        self.menu_items = []
        self.setting: int
        super().__init__(name, description)

    def apply_chosen_option(self):
        if self.user_input == 1:
            self.setting = True
        elif self.user_input == 2:
            self.setting = False
        
class NavigationMenu(NumberedMenu):
    def __init__(self, name, description):
        super().__init__(name, description)
    
    def start(self):
        menu_name_array = []
        for menu in self.options:
            menu_name_array.append(menu.name)
        self.menu_items = menu_name_array
        self.draw_menu()
        
    def apply_chosen_option(self):
        self.options[self.user_input - 1].start()
