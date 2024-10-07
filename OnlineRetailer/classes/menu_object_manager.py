from classes.text_input_menu import LoginMenu, RegistrationMenu
from classes.numbered_menu import NavigationMenu, SettingBoolMenu

class MenuObjectManager():
    DEFAULT_DESCRIPTION = "Please select the desired menu."
    SECURITY_DESCRIPTION = "Please select the desired security setting."
    REGISTRATION_DESCRIPTION = "Please create a new username and password."
    LOGIN_DESCRIPTION = "Please input your username and password."
    
    def __init__(self, account_manager, database_manager):
        self.security_menu = SettingBoolMenu("Security Mode", self.SECURITY_DESCRIPTION, account_manager)     
        self.landing_menu = NavigationMenu("Landing", self.DEFAULT_DESCRIPTION, account_manager)
        self.registration_menu = RegistrationMenu("Sign Up", self.REGISTRATION_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu)
        self.login_menu = LoginMenu("Login", self.LOGIN_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu)
