from classes.logout_option import LogoutOption
from classes.security_menu_option import SecurityMenuOption
from classes.text_input_menu import LoginMenu, RegistrationMenu
from classes.numbered_menu import NavigationMenu

class MenuObjectManager():
    DEFAULT_DESCRIPTION = "Please select the desired menu."
    SECURITY_DESCRIPTION = "Please select the desired security setting."
    PRODUCTS_DESCRIPTION = "Please select the desired product."
    REGISTRATION_DESCRIPTION = "Please create a new username and password."
    LOGIN_DESCRIPTION = "Please input your username and password."
    LOGOUT_DESCRIPTION = "Are you sure you want to log out?"
    
    
    def __init__(self, account_manager, database_manager, security_manager):
        self.security_menu = NavigationMenu("Security Mode", self.SECURITY_DESCRIPTION, account_manager)
        self.security_on_option = SecurityMenuOption("Security ON", "Security mode has been turned on.", account_manager, security_manager, True)
        self.security_off_option = SecurityMenuOption("Security OFF", "Security mode has been turned off.", account_manager, security_manager, False)
        
        self.landing_menu = NavigationMenu("Landing Page", self.DEFAULT_DESCRIPTION, account_manager)
        
        self.logout_option = LogoutOption("Log Out", self.LOGOUT_DESCRIPTION, account_manager, self.landing_menu)
        self.account_settings_menu = NavigationMenu("Account Settings", "Change your account settings here.", account_manager)
        self.payment_settings_menu = NavigationMenu("Payment Settings", "Change your payment details here.", account_manager)

        self.products_menu = NavigationMenu("Products", self.PRODUCTS_DESCRIPTION, account_manager)
        self.product1_menu = NavigationMenu("Product1", "" , account_manager)
        self.product2_menu = NavigationMenu("Product2", "" , account_manager)

        self.registration_menu = RegistrationMenu("Sign Up", self.REGISTRATION_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu)
        self.login_menu = LoginMenu("Login", self.LOGIN_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu)

        #Define menu paths:
        self.DEFAULT_LANDING_OPTIONS = [self.registration_menu, self.login_menu]
        self.USER_LANDING_OPTIONS = [self.products_menu, self.logout_option, self.account_settings_menu]

        self.security_menu.options = [self.security_on_option, self.security_off_option]
        
        self.landing_menu.options = [self.registration_menu, self.login_menu]
        
        self.account_settings_menu.options = [self.payment_settings_menu]
        
        self.products_menu.options = [self.landing_menu, self.product1_menu, self.product2_menu]
        self.product1_menu.options = [self.landing_menu]
        self.product2_menu.options = [self.landing_menu]

    def guest_menu_options(self):
        self.landing_menu.options = self.DEFAULT_LANDING_OPTIONS
        
    def user_menu_options(self):
        self.landing_menu.options = self.USER_LANDING_OPTIONS
        
    def admin_menu_options(self):
        self.landing_menu.options = self.USER_LANDING_OPTIONS