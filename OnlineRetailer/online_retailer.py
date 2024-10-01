from classes.account_manager import AccountManager
from classes.database_manager import DatabaseManager
from classes.text_input_menu import LoginMenu, RegistrationMenu
from classes.numbered_menu import NavigationMenu, SettingBoolMenu

DEFAULT_DESCRIPTION = "Please select the desired menu."
SECURITY_DESCRIPTION = "Please select the desired security setting."
REGISTRATION_DESCRIPTION = "Please create a new username and password."
LOGIN_DESCRIPTION = "Please input your username and password."
#Declare objects:

account_manager = AccountManager()
database_manager = DatabaseManager()
database_manager.print_user_data() #debug
security_menu = SettingBoolMenu("Security Mode", SECURITY_DESCRIPTION, account_manager)     
landing_menu = NavigationMenu("Landing", DEFAULT_DESCRIPTION, account_manager)
registration_menu = RegistrationMenu("Sign Up", REGISTRATION_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, landing_menu)
login_menu = LoginMenu("Login", LOGIN_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, landing_menu)

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
