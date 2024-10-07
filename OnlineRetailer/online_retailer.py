from classes.account_manager import AccountManager
from classes.database_manager import DatabaseManager
from classes.menu_object_manager import MenuObjectManager

account_manager = AccountManager()
database_manager = DatabaseManager()
menu_object_manager = MenuObjectManager()
database_manager.print_user_data() #debug

#Define menu paths:
security_menu.menu_items = ["Security ON", "Security OFF"]
landing_menu.options = [registration_menu, login_menu]


#TODO: Change settings depending on security and login here
    

#Login:

def login(user_type):
    logged_in = True
    admin = False
    print("hi")

#Security:
security_menu.start()
security = security_menu.setting

#Start:
landing_menu.start()
