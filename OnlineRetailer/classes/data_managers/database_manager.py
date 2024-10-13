"""This module houses the DatabaseManager class."""
import csv
from classes.menu_options.user_list_option import UserListOption
class DatabaseManager:
    """Handles all editing of the CSV account database."""

    database = "database/account_data_secure.csv"

    def create_secure_account(self, username, password, salt):
        """Writes new account to secure database"""
        with open(self.database, "a", encoding="utf-8", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, "FALSE", password, salt, "", ""])
        csvfile.close()

    def create_insecure_account(self, username, password):
        """Writes new account to insecure database"""
        with open(self.database, "a", encoding="utf-8", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, "FALSE", password, ""])
        csvfile.close()

    def is_username_taken(self, username):
        """Checks if username is taken and returns username row if so."""
        with open(self.database, "r", encoding="utf-8", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Username"] == username:
                    return row
            csvfile.close()
            return False

    def find_user_row(self, username):
        """Receives username and returns the row of the user."""
        csvfile = open(self.database, "r", encoding="utf-8", newline = "")
        reader = csv.reader(csvfile)
        data_list = list(reader)
        for i, row in enumerate(data_list):
            if row[0] == username:
                csvfile.close()
                return[data_list, i]

    def rewrite_file(self, data_list):
        """Writes given list data into the CSV."""
        csvfile = open(self.database, "w", encoding="utf-8", newline = "")
        writer = csv.writer(csvfile)
        writer.writerows(data_list)
        csvfile.close()

    def add_card_details_secure(self, username, card_details, salt):
        """Adds card details to secure database."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][4] = card_details
        data_list[i][5] = salt
        self.rewrite_file(data_list)

    def add_card_details_insecure(self,username, card_details):
        """Adds card details to insecure database."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][3] = card_details
        self.rewrite_file(data_list)

    def remove_card_details(self, account):
        """Removes card details from database."""
        data = self.find_user_row(account.username)
        data_list = data[0]
        i = data[1]
        #Check for secure/insecure database:
        if self.database == "database/account_data_secure.csv":
            data_list[i][4] = None
            data_list[i][5] = None
        else:
            data_list[i][3] = None
        self.rewrite_file(data_list)

    def change_password_secure(self, username, password, salt):
        """Changes to new user password within secure database."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][2] = password
        data_list[i][3] = salt
        self.rewrite_file(data_list)

    def change_password_insecure(self,username,password):
        """Changes to new user password within insecure database."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][2] = password
        self.rewrite_file(data_list)

    def get_user_list(self, account, landing):
        """Returns user list for admin use."""
        csvfile = open(self.database, "r", encoding="utf-8", newline = "")
        reader = csv.reader(csvfile)
        data_list = list(reader)
        user_option_array = []
        for i, row in enumerate(data_list):
            if i != 0 and row[0] != account.username:
                user_option = UserListOption(row[0], "", account, landing, self)
                user_option_array.append(user_option)
        user_option_array.append(landing)
        return user_option_array

    def get_user_count(self):
        """Returns the total user count for currently
        accessed database."""
        csvfile = open(self.database, "r", encoding="utf-8", newline = "")
        reader = csv.reader(csvfile)
        data_list = list(reader)
        return len(data_list) - 1 #Subtract the top row

    def is_user_admin(self, username):
        """Checks if user is admin."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        if data_list[i][1] == "TRUE":
            return True
        return False

    def delete_user(self,username):
        """Deletes user row from database."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list.pop(i)
        self.rewrite_file(data_list)

    def promote_to_admin(self, username):
        """Sets Admin cell to TRUE."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][1] = "TRUE"
        self.rewrite_file(data_list)

    def demote_from_admin(self, username):
        """Sets Admin cell to FALSE."""
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][1] = "FALSE"
        self.rewrite_file(data_list)
