import csv
class DatabaseManager:

    def create_account(self, username, password, salt):
        with open("database/account_data.csv", "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, "False", password, salt, "", ""])
        csvfile.close()
    
    def is_username_taken(self, username):
        with open("database/account_data.csv", "r", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Username"] == username:
                    return row
            csvfile.close()
            return False
            
    def print_user_data(self):
        with open("database/account_data.csv", "r", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
        csvfile.close()
    
    def find_user_row(self, username):
        csvfile = open("database/account_data.csv", "r", newline = "")
        reader = csv.reader(csvfile)
        data_list = list(reader)
        for i, row in enumerate(data_list):
            if row[0] == username:
                csvfile.close()
                return[data_list, i]
            
    def rewrite_file(self, data_list):
        csvfile = open("database/account_data.csv", "w", newline = "")
        writer = csv.writer(csvfile)
        writer.writerows(data_list)
        csvfile.close()

    def add_card_details(self, username, card_details, salt):
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][4] = card_details
        data_list[i][5] = salt
        self.rewrite_file(data_list)               

    def remove_card_details(self, account):
        data = self.find_user_row(account.username)
        data_list = data[0]
        i = data[1]
        data_list[i][4] = None
        data_list[i][5] = None
        self.rewrite_file(data_list)
        
    def change_password(self, username, password, salt):
        data = self.find_user_row(username)
        data_list = data[0]
        i = data[1]
        data_list[i][2] = password
        data_list[i][3] = salt
        self.rewrite_file(data_list)