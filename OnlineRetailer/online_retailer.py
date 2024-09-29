from classes.database_manager import DatabaseManager
from classes.text_input_menu import LoginMenu, RegistrationMenu
from classes.numbered_menu import NavigationMenu, SettingBoolMenu
from classes.hasher import Hasher

DEFAULT_DESCRIPTION = "Please select the desired menu."
SECURITY_DESCRIPTION = "Please select the desired security setting."
REGISTRATION_DESCRIPTION = "Please create a new username and password."
LOGIN_DESCRIPTION = "Please input your username and password."
#Declare objects:

database_manager = DatabaseManager()
database_manager.print_user_data() #debug
security_menu = SettingBoolMenu("Security Mode", SECURITY_DESCRIPTION)     
landing_menu = NavigationMenu("Landing", DEFAULT_DESCRIPTION)
registration_menu = RegistrationMenu("Sign Up", REGISTRATION_DESCRIPTION, ["Username" , "Password"], database_manager)
login_menu = LoginMenu("Login", LOGIN_DESCRIPTION, ["Username" , "Password"], database_manager)

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
