from classes.menu_classes.menu import Menu
from classes.hasher import Hasher
import os
import re

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
        self.user_input = []
        print("Account created successfully!")
        
class LoginMenu(TextInputMenu):
    user_data = []    

    def apply_user_input(self):
        self.account.login(self.user_data["Username"], self.user_data["Admin"])
    
    def input_restriction(self, user_input, query):
        if query == "Username":
           self.user_data = self.database_manager.is_username_taken(user_input)
           if self.user_data == False:
               print("Invalid Username.")
           return self.user_data
        if query == "Password":
            if str(Hasher.hash(user_input, eval(self.user_data["Salt"]))) == self.user_data["Password"]:
                print("Welcome, " , self.user_data["Username"])
                return True
            print("Incorrect Password.")
            return False

class ChangePassword(TextInputMenu):
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu):
        self.database_manager = database_manager
        super().__init__(name, description, account, input_queries, database_manager, previous_menu)

    def apply_user_input(self):
        salt = os.urandom(32)
        password_hash = Hasher.hash(self.user_input[1], salt)
        self.database_manager.change_password(self.user_data["Username"], password_hash, salt)
    
    def input_restriction(self, user_input, query):
        self.user_data = self.database_manager.is_username_taken(self.account.username)
        if query == "Old Password":
            if str(Hasher.hash(user_input, eval(self.user_data["Salt"]))) == self.user_data["Password"]:
                return True
            print("Old password incorrect.")
            return False
        if query == "New Password":
            return self.password_input_restriction()
    
    def password_input_restriction(self):
        return True
        print("Password has been changed successfully.")

class AddCardMenu(TextInputMenu):
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu):
        self.input_queries = input_queries
        self.user_input = []
        self.database_manager = database_manager
        self.previous_menu = previous_menu
        super().__init__(name, description, account, input_queries, database_manager, previous_menu)
        
    def input_restriction(self, user_input, query):
        if query == "First Name" or query == "Last Name":
           return self.name_restriction(user_input)
        if query == "Card Number (Without Hyphens)":
           return self.card_number_restriction(user_input)
        if query == "Expiration Date (mm/yy)":
           return self.exp_date_restriction(user_input)
        if query == "CVC Code":
           return self.cvc_restriction(user_input)
    
    def name_restriction(self, user_input):
        if len(user_input) > 40:
            print("Name entry too long.")
            return False
        x = re.findall("[0-9]", user_input)
        if x:
            print("Invalid name entry.")
            return False
        return True

    def card_number_restriction(self, user_input):
        try:
            int(user_input)
        except ValueError:
            print("Invalid card number value type.")
            return False
        if len(user_input) != 16:
            print("Invalid card number entry.")
            return False
        return True

    def exp_date_restriction(self, user_input):
        x = re.fullmatch("[0-1][0-9]\/[0-9]{2}" , user_input)
        if x:
            mm = user_input[0] + user_input[1]
            yy = user_input[3] + user_input[4]
            if mm[0] == "0":
                mm = mm[1]
            mm = eval(mm)
            if mm >= 1 and mm <= 12:
                return True
        print("Invalid expiration date entry.")
        return False

    def cvc_restriction(self, user_input):
        try:
            int(user_input)
        except ValueError:
            print("Invalid CVC value type.")
            return False
        if len(user_input) != 3:
            print("Invalid VCV entry.")
            return False
        return True

    def apply_user_input(self):
        first_name = self.user_input[0].capitalize()
        last_name = self.user_input[1].capitalize()
        card_num = self.user_input[2]
        exp_date = self.user_input[3]
        cvc = self.user_input[4]
        hashable_string = first_name + "," + last_name + "," + card_num + "," + exp_date + "," + cvc
        salt = os.urandom(32)
        card_hash = Hasher.hash(hashable_string, salt)
        self.database_manager.add_card_details(self.account.username, card_hash, salt)
        print("Card details added to account successfully.")


