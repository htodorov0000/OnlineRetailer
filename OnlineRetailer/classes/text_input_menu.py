from classes.menu import Menu

class TextInputMenu(Menu):
    def __init__(self, name, description, input_queries):
        self.input_queries = input_queries
        self.user_input = []
        super().__init__(name, description)

    def draw_menu(self):
        while True:
            self.draw_name_and_description()
            for query in self.input_queries:
                user_input = input(query + ": ")
                self.user_input.append(user_input)
            self.apply_user_input()

    def apply_user_input(self):
        pass

class RegistrationMenu(TextInputMenu):
    def apply_user_input(self):
        pass #write username and password
    
class LoginMenu(TextInputMenu):
    def apply_user_input(self):
        pass #check username and password



