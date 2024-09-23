from classes.text_input_menu import LoginMenu, RegistrationMenu
from classes.numbered_menu import NavigationMenu, SettingBoolMenu

DEFAULT_DESCRIPTION = "Please select the desired menu."
SECURITY_DESCRIPTION = "Please select the desired security setting."
REGISTRATION_DESCRIPTION = "Please create a new username and password."
LOGIN_DESCRIPTION = "Please input your username and password."
#Declare menu objects:

security_menu = SettingBoolMenu("Security Mode", SECURITY_DESCRIPTION)     
landing_menu = NavigationMenu("Landing", DEFAULT_DESCRIPTION)
registration_menu = RegistrationMenu("Sign Up", REGISTRATION_DESCRIPTION, ["Username" , "Password"])
login_menu = LoginMenu("Login", LOGIN_DESCRIPTION, ["Username" , "Password"])


#Define menu paths:
security_menu.menu_items = ["Security ON", "Security OFF"]
landing_menu.options = [registration_menu, login_menu]


#Security:
security_menu.start()
security = security_menu.setting

#TODO: Change settings depending on security and login here



#Start:
landing_menu.start()
