class NumberedMenu:
    INVALID_INPUT: str = "Invalid input type. Try again."
    INVALID_RANGE: str = "Please input a number in the correct range."
    def __init__(self, name):
        self.name = name
        self.user_input: int
        self.menu_items = []
    
    def start(self):
        self.draw_menu()

    def draw_menu(self):
        menu_string = ""
        for num, menu_item in enumerate(self.menu_items):
            menu_string += (str(num + 1) + ". " + menu_item + """
""")
        while True:
            try:
                self.user_input = int(input(menu_string))
                if self.user_input < len(self.menu_items) and self.user_input > 0:
                    break
                else:
                    print(self.INVALID_RANGE)
            except ValueError:
                print(self.INVALID_INPUT)
        self.apply_chosen_option()
                
    def apply_chosen_option(self):
        pass
    
class SettingBoolMenu(NumberedMenu):   
    def __init__(self, name):
        self.menu_items = []
        self.setting: int
        return super().__init__(name)

    def apply_chosen_option(self):
        if self.user_input == 1:
            self.setting = True
        elif self.user_input == 2:
            self.setting = False
        
class NavigationMenu(NumberedMenu):
    def __init__(self, name):
        self.menus = []
        return super().__init__(name)
    
    def start(self):
        menu_name_array = []
        for menu in self.menus:
            menu_name_array.append(menu.name)
        self.menu_items = menu_name_array
        self.draw_menu()
        
    def apply_chosen_option(self):
        self.menus[self.user_input - 1].start()
            

security_menu = SettingBoolMenu("Security Menu")     
test_nav_menu1 = NavigationMenu("TestNavMenu1")
test_nav_menu2 = NavigationMenu("TestNavMenu2")
test_nav_menu3 = NavigationMenu("TestNavMenu3")
test_nav_menu4 = NavigationMenu("TestNavMenu4")

security_menu.menu_items = ["Security ON", "Security OFF"]
test_nav_menu1.menus = [test_nav_menu2, test_nav_menu3, test_nav_menu4]
test_nav_menu2.menus = [test_nav_menu1, test_nav_menu3, test_nav_menu4]
test_nav_menu3.menus = [test_nav_menu1, test_nav_menu2, test_nav_menu4]

security_menu.start()
print(security_menu.setting)
test_nav_menu1.start()

