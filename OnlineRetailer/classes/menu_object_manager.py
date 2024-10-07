from classes.text_input_menu import LoginMenu, RegistrationMenu
from classes.numbered_menu import NavigationMenu, SettingBoolMenu

class MenuObjectManager():
    DEFAULT_DESCRIPTION = "Please select the desired menu."
    SECURITY_DESCRIPTION = "Please select the desired security setting."
    PRODUCTS_DESCRIPTION = "Please select the desired product."
    REGISTRATION_DESCRIPTION = "Please create a new username and password."
    LOGIN_DESCRIPTION = "Please input your username and password."
    
    def __init__(self, account_manager, database_manager):
        self.security_menu = SettingBoolMenu("Security Mode", self.SECURITY_DESCRIPTION, account_manager)     
        self.landing_menu = NavigationMenu("Landing", self.DEFAULT_DESCRIPTION, account_manager)
        self.products_menu = NavigationMenu("Products", self.PRODUCTS_DESCRIPTION, account_manager)
        self.product1_menu = NavigationMenu("Product1", "" , account_manager)
        self.product2_menu = NavigationMenu("Product2", "" , account_manager)

        self.registration_menu = RegistrationMenu("Sign Up", self.REGISTRATION_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu)
        self.login_menu = LoginMenu("Login", self.LOGIN_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu)

        #Define menu paths:
        self.security_menu.menu_items = ["Security ON", "Security OFF"]
        self.landing_menu.options = [self.registration_menu, self.login_menu]
        self.products_menu.options = [self.landing_menu, self.product1_menu, self.product2_menu]
        self.product1_menu.options = [self.landing_menu]
        self.product2_menu.options = [self.landing_menu]        

    def guest_menu_options(self):
        self.landing_menu.options = [self.registration_menu, self.login_menu]
        
    def user_menu_options(self):
        self.landing_menu.options = [self.products_menu, self.registration_menu, self.login_menu]
        
    def admin_menu_options(self):
        self.landing_menu.options = [self.products_menu, self.registration_menu, self.login_menu]