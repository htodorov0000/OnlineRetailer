from classes.menu import Menu
from classes.hasher import Hasher
class TextInputMenu(Menu):
    def __init__(self, name, description, input_queries, database_manager):
        self.input_queries = input_queries
        self.user_input = []
        self.database_manager = database_manager
        super().__init__(name, description)

    def draw_menu(self):
        self.draw_name_and_description()
        for query in self.input_queries:
            while True:
                user_input = input(query + ": ")
                if self.input_restriction(user_input, query):
                    self.user_input.append(user_input)
                    break
        self.apply_user_input()

    def input_restriction(self, user_input, query):
        return True

    def apply_user_input(self):
        pass

class RegistrationMenu(TextInputMenu):
    USERNAME_MIN_LENGTH = 3
    USERNAME_MAX_LENGTH = 16

    def input_restriction(self, user_input, query):
        if query == "Username":
            return self.username_input_restriction(user_input)
        elif query == "Password":
            return self.password_input_restriction(user_input)
            
    def username_input_restriction(self, username):
        if len(username) < self.USERNAME_MIN_LENGTH or len(username) > self.USERNAME_MAX_LENGTH:
            print("Username must be between ", str(self.USERNAME_MIN_LENGTH), " and ", str(self.USERNAME_MAX_LENGTH), " characters long.")
            return False
        if self.database_manager.is_username_taken(username):
            print("Username is already taken.")
            return False
        return True
    
    def password_input_restriction(self, user_input):
        return True

    def apply_user_input(self):
        username = self.user_input[0]
        password = Hasher.hash(self.user_input[1])
        self.database_manager.create_account(username, password)
        
class LoginMenu(TextInputMenu):
    def apply_user_input(self):
        pass #check username and password



