from classes.menu import Menu
from classes.hasher import Hasher
import os

class TextInputMenu(Menu):
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu):
        self.input_queries = input_queries
        self.user_input = []
        self.database_manager = database_manager
        self.previous_menu = previous_menu
        super().__init__(name, description, account)

    def draw_menu(self):
        self.draw_name_and_description()
        for query in self.input_queries:
            user_input = input(query + ": ")
            if self.input_restriction(user_input, query):
                self.user_input.append(user_input)
            else:
                self.previous_menu.start()
        self.apply_user_input()
        self.previous_menu.start()

    def input_restriction(self, user_input, query):
        return True

    def apply_user_input(self):
        pass
    

class RegistrationMenu(TextInputMenu):
    USERNAME_MIN_LENGTH = 6
    USERNAME_MAX_LENGTH = 20

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
        salt = os.urandom(32)
        password_hash = Hasher.hash(self.user_input[1], salt)
        self.database_manager.create_account(username, password_hash, salt)
        print("Account created successfully!")
        
class LoginMenu(TextInputMenu):
    user_data = []    

    def apply_user_input(self):
        self.account.login(self.user_data["Username"], self.user_data["Admin"])
    
    def input_restriction(self, user_input, query):
        if query == "Username":
           self.user_data = self.database_manager.is_username_taken(user_input)
           return self.user_data
        if query == "Password":
            if str(Hasher.hash(user_input, eval(self.user_data["Salt"]))) == self.user_data["Password"]:
                print("Welcome, " , self.user_data["Username"])
                return True
            return False



