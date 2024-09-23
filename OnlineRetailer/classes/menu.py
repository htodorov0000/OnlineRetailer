class Menu:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def start(self):
        self.draw_menu()
    
    def draw_name_and_description(self):
        print()
        print("***" + self.name.upper() + "***")
        print()
        if self.description != "": #Print description if it isn't empty.
            print(self.description)
            print()

    def draw_menu(self):
        self.draw_name_and_description()
                

