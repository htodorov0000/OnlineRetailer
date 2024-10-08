class Menu:
    def __init__(self, name, description, account):
        self.name = name
        self.description = description
        self.account = account
        self.options = []
    
    def start(self):
        self.draw_menu()
    
    def draw_name_and_description(self):
        print()
        if self.account.logged_in:
            print("                                                 User:", self.account.username)
        else: 
            print("                                                 Guest")
        if self.account.admin:
            print("                                                 (Admin Account)")
        print()
        print("***" + self.name.upper() + "***")
        print()
        if self.description != "": #Print description if it isn't empty.
            print(self.description)
            print()

    def draw_menu(self):
        self.draw_name_and_description()
                

