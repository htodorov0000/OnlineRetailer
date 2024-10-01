class AccountManager:
    def __init__(self):
        self.logged_in = False
        self.username = ""
        self.admin = False
    
    def login(self, username, admin):
        self.username = username
        self.admin = eval(admin.capitalize())
        self.logged_in = True

    def log_out(self):
        self.username = ""
        self.admin = False
        self.logged_in = False
    
