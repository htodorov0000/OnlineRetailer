"""This module houses Menu classes which receive
text inputs."""

import os
import re
import time
from classes.menu_classes.menu import Menu

class TextInputMenu(Menu):
    """Base text input menu to be extended from."""
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu):
        self.input_queries = input_queries
        self.user_input = []
        self.database_manager = database_manager
        self.previous_menu = previous_menu
        super().__init__(name, description, account)

    def draw_menu(self):
        """Draws menu including multiple queries and
        asks for input."""
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
        """To be used in child classes for
        restricting input."""
        return True

    def apply_user_input(self):
        """To be used in child classes for applying
        given user input."""
        


class RegistrationMenu(TextInputMenu):
    """Text input menu used for registering user account."""
    USERNAME_MIN_LENGTH = 6
    USERNAME_MAX_LENGTH = 20
    MAX_ACCOUNTS_IN_DATABASE = 10

    def __init__(self, name, description, account, input_queries, database_manager, previous_menu, security_manager, hasher):
        self.security_manager = security_manager
        self.hasher = hasher
        self.has_user_created_account = False
        super().__init__(name, description, account, input_queries, database_manager, previous_menu)

    def start(self):
        """Called when menu is to be drawn."""
        #Check if account limit is reached:
        if self.database_manager.get_user_count() >= self.MAX_ACCOUNTS_IN_DATABASE:
            print("Maximum number of accounts reached. Please try again later.")
            self.previous_menu.start()
        #In security mode, check if user has already created account:
        if self.security_manager.security and self.has_user_created_account:
            print("Only one account allowed to be created per user.")
            self.previous_menu.start()
        super().start()

    def input_restriction(self, user_input, query):
        """Checks if user input is valid."""
        if query == "Username":
            return self.username_input_restriction(user_input)
        return self.password_input_restriction(user_input)

    def username_input_restriction(self, username):
        """Checks if registration username is valid and not taken."""
        if self.security_manager.security:
            #Escape characters which allow CSV injections:
            if "=" in username or "+" in username or "-" in username or "@" in username or "," in username or ";" in username or "'" in username or '"' in username or " " in username or "\t" in username:
                print("The following characters are not allowed in a username: =+-@,;'" + '"' + "spaces, tabs.")
                return False
        if len(username) < self.USERNAME_MIN_LENGTH or len(username) > self.USERNAME_MAX_LENGTH:
            print("Username must be between ", str(self.USERNAME_MIN_LENGTH), " and ", str(self.USERNAME_MAX_LENGTH), " characters long.")
            return False
        if self.database_manager.is_username_taken(username):
            print("Username is already taken.")
            return False
        return True

    def password_input_restriction(self, user_input):
        """Checks if password matches strength requirements
        if security mode is on."""
        if self.security_manager.security:
            if not re.fullmatch("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{12,}$", user_input):
                print("Password too weak. Passwords require 12+ characters, an uppercase and lowercase letter, a number, and a special character (#?!@$%^&*-)")
                return False
        return True

    def apply_user_input(self):
        """Asks DatabaseManager to write account data
        for the successfully registered user."""
        if self.security_manager.security:
            username = self.user_input[0]
            salt = os.urandom(32)
            password_hash = self.hasher.hash(self.user_input[1], salt)
            self.database_manager.create_secure_account(username, password_hash, salt)
        else:
            self.database_manager.create_insecure_account(self.user_input[0], self.user_input[1])
        print("Account created successfully!")
        self.user_input = []
        self.has_user_created_account = True

class LoginMenu(TextInputMenu):
    """Text input menu class for handling login process."""
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu, security_manager, hasher):
        self.security_manager = security_manager
        self.user_data = []
        self.remaining_login_attempts = 3
        self.hasher = hasher
        super().__init__(name, description, account, input_queries, database_manager, previous_menu)

    def apply_user_input(self):
        """Logs in user with correct credentials."""
        self.account.login(self.user_data["Username"], self.user_data["Admin"])

    def input_restriction(self, user_input, query):
        """Checks if username and password are matching."""
        if query == "Username":
            self.user_data = self.database_manager.is_username_taken(user_input)
            if not self.user_data:
                print("Invalid Username.")
                if self.security_manager.security:
                    self.remaining_login_attempts -= 1
                    self.limit_login_attempt()
            return self.user_data
        if query == "Password":
            if self.security_manager.security:
                return self.password_input_restriction_secure(user_input)
            return self.password_input_restriction_insecure(user_input)

    def password_input_restriction_secure(self, user_input):
        """Hashes given password and compares with stored 
        password hash when security mode is on."""
        if str(self.hasher.hash(user_input, eval(self.user_data["Salt"]))) == self.user_data["Password"]:
            print("Welcome, " , self.user_data["Username"])
            return True
        print("Incorrect Password.")
        if self.security_manager.security:
            self.remaining_login_attempts -= 1
            self.limit_login_attempt()
        return False

    def password_input_restriction_insecure(self, user_input):
        """Compares given password with stored password when
        security mode is off."""
        if user_input == self.user_data["Password"]:
            print("Welcome, " , self.user_data["Username"])
            return True
        print("Incorrect Password.")
        return False

    def limit_login_attempt(self):
        """Prevents brute-force attacks by timing out users who
        enter incorrect login credentials multiple times."""
        if self.remaining_login_attempts <= 0:
            print("Too many failed login attempts. Please wait 1 minute before attempting another login.")
            self.remaining_login_attempts = 3
            time.sleep(60)
            print("The time has elapsed, please attempt to log in again.")
            self.previous_menu.start()

class ChangePassword(TextInputMenu):
    """Text input menu class for changing user password."""
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu, security_manager, hasher):
        self.database_manager = database_manager
        self.security_manager = security_manager
        self.hasher = hasher
        super().__init__(name, description, account, input_queries, database_manager, previous_menu)

    def apply_user_input(self):
        """Changes password if successfully matched conditions."""
        if self.security_manager.security:
            self.change_password_secure()
        else:
            self.change_password_insecure()

    def change_password_secure(self):
        """Changes password when security mode is on."""
        salt = os.urandom(32)
        password_hash = self.hasher.hash(self.user_input[1], salt)
        self.database_manager.change_password_secure(self.user_data["Username"], password_hash, salt)

    def change_password_insecure(self):
        """Changes password when security mode is off."""
        self.database_manager.change_password_insecure(self.user_data["Username"], self.user_input[1])

    def input_restriction(self, user_input, query):
        """Checks if old password is correct and if new password is
        valid."""
        self.user_data = self.database_manager.is_username_taken(self.account.username)
        if query == "Old Password":
            if self.security_manager.security:
                if str(self.hasher.hash(user_input, eval(self.user_data["Salt"]))) == self.user_data["Password"]:
                    return True
            else:
                if self.user_data["Password"] == user_input:
                    return True
            print("Old password incorrect.")
            return False
        if query == "New Password":
            return self.password_input_restriction(user_input)

    def password_input_restriction(self, user_input):
        """Checks if password is strong enough if security mode is on."""
        if self.security_manager.security:
            if not re.fullmatch("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{12,}$", user_input):
                print("Password too weak. Passwords require 12+ characters, an uppercase and lowercase letter, a number, and a special character (#?!@$%^&*-)")
                return False
        print("Password has been changed successfully.")
        return True


class AddCardMenu(TextInputMenu):
    """Text input menu class for allowing user to add payment credentials."""
    def __init__(self, name, description, account, input_queries, database_manager, previous_menu, security_manager, hasher):
        self.input_queries = input_queries
        self.user_input = []
        self.database_manager = database_manager
        self.previous_menu = previous_menu
        self.security_manager = security_manager
        self.hasher = hasher
        super().__init__(name, description, account, input_queries, database_manager, previous_menu)

    def input_restriction(self, user_input, query):
        """Checks if inputted data is valid."""
        if query == "First Name" or query == "Last Name":
            return self.name_restriction(user_input)
        if query == "Card Number (Without Hyphens)":
            return self.card_number_restriction(user_input)
        if query == "Expiration Date (mm/yy)":
            return self.exp_date_restriction(user_input)
        if query == "CVC Code":
            return self.cvc_restriction(user_input)

    def name_restriction(self, user_input):
        """Restricts First/Last name character count and types."""
        if len(user_input) > 40:
            print("Name entry too long.")
            return False
        x = re.findall("[0-9]", user_input)
        if x:
            print("Invalid name entry.")
            return False
        return True

    def card_number_restriction(self, user_input):
        """Restricts card number to correct amount of digits and value type."""
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
        """Restricts expiration date input to correct format."""
        x = re.fullmatch("[0-1][0-9]\/[0-9]{2}" , user_input)
        if x:
            mm = user_input[0] + user_input[1]
            if mm[0] == "0":
                mm = mm[1]
            mm = eval(mm)
            if mm >= 1 and mm <= 12:
                return True
        print("Invalid expiration date entry.")
        return False

    def cvc_restriction(self, user_input):
        """Restricts CVC input to correct format."""
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
        """Requests for the database to write card data."""
        first_name = self.user_input[0].capitalize()
        last_name = self.user_input[1].capitalize()
        card_num = self.user_input[2]
        exp_date = self.user_input[3]
        cvc = self.user_input[4]
        data_string = first_name + "," + last_name + "," + card_num + "," + exp_date + "," + cvc
        if self.security_manager.security:
            self.apply_user_input_secure(data_string)
        else:
            self.apply_user_input_insecure(data_string)

    def apply_user_input_secure(self, hashable_string):
        """Requests hasher to hash card data securely when security
        mode is on."""
        salt = os.urandom(32)
        card_hash = self.hasher.hash(hashable_string, salt)
        self.database_manager.add_card_details_secure(self.account.username, card_hash, salt)
        print("Card details added to account successfully.")

    def apply_user_input_insecure(self, data_string):
        """Insecurely requests for the data to be written to database."""
        self.database_manager.add_card_details_insecure(self.account.username, data_string)
