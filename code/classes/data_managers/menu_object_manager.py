"""This module houses the MenuObjectManager class."""

from classes.hasher import Hasher
from classes.menu_classes.user_list_menu import UserListMenu
from classes.menu_options.buy_option import BuyOption
from classes.menu_options.remove_card_details_option import RemoveCardDetailsOption
from classes.menu_options.logout_option import LogoutOption
from classes.menu_options.security_menu_option import SecurityMenuOption
from classes.menu_classes.text_input_menu import AddCardMenu, ChangePassword, LoginMenu, RegistrationMenu
from classes.menu_classes.numbered_menu import NavigationMenu
from classes.menu_classes.product import Product

class MenuObjectManager():
    """The instance of this class creates and manages all menu objects,
    sets their paths and parameters."""

    DEFAULT_DESCRIPTION = "Please select the desired menu."
    SECURITY_DESCRIPTION = "Please select the desired security setting."
    PRODUCTS_DESCRIPTION = "Please select the desired product."
    REGISTRATION_DESCRIPTION = "Please create a new username and password."
    LOGIN_DESCRIPTION = "Please input your username and password."
    LOGOUT_DESCRIPTION = "Are you sure you want to log out?"


    def __init__(self, account_manager, database_manager, security_manager):
        self.hasher = Hasher()

        #Create menu objects:
        self.security_menu = NavigationMenu("Security Mode", self.SECURITY_DESCRIPTION, account_manager)
        self.security_on_option = SecurityMenuOption("Security ON", "Security mode has been turned on.", account_manager, security_manager, True)
        self.security_off_option = SecurityMenuOption("Security OFF", "Security mode has been turned off.", account_manager, security_manager, False)

        self.landing_menu = NavigationMenu("Landing Page", self.DEFAULT_DESCRIPTION, account_manager)

        self.logout_option = LogoutOption("Log Out", self.LOGOUT_DESCRIPTION, account_manager, self.landing_menu)
        self.account_settings_menu = NavigationMenu("Account Settings", "Change your account settings here.", account_manager)
        self.change_password_option = ChangePassword("Change Password", "Change your password", account_manager, ["Old Password", "New Password"],\
            database_manager, self.account_settings_menu, security_manager, self.hasher)
        self.add_new_card_option = AddCardMenu("Add New Card", "Add new card (note: this will overwrite any previous card details).", account_manager,\
            ["First Name", "Last Name", "Card Number (Without Hyphens)", "Expiration Date (mm/yy)", "CVC Code"] , database_manager, self.account_settings_menu, security_manager, self.hasher)
        self.remove_card_option = RemoveCardDetailsOption("Remove Card", "Remove card currently on account.", account_manager, database_manager, self.account_settings_menu)

        self.user_list_menu = UserListMenu("(ADMIN ONLY) User List", "Please select a user (ADMIN ONLY MENU).", account_manager, database_manager, self.landing_menu)

        self.products_menu = NavigationMenu("Products", self.PRODUCTS_DESCRIPTION, account_manager)
        self.buy = BuyOption("Buy", "desc", account_manager, database_manager, self.products_menu)
        self.product1_menu = Product("Product 1", "Product Description.", account_manager, 49.99, self.buy, self.products_menu)
        self.product2_menu = Product("Product 2", "Product Description.", account_manager, 12.99, self.buy, self.products_menu)

        self.registration_menu = RegistrationMenu("Sign Up", self.REGISTRATION_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, \
            self.landing_menu, security_manager, self.hasher)
        self.login_menu = LoginMenu("Login", self.LOGIN_DESCRIPTION, account_manager, ["Username" , "Password"], database_manager, self.landing_menu, security_manager, self.hasher)

        #Define menu paths:
        self.default_landing_options = [self.registration_menu, self.login_menu]
        self.user_landing_options = [self.products_menu, self.account_settings_menu, self.logout_option]
        self.admin_landing_options = [self.products_menu, self.account_settings_menu, self.user_list_menu , self.logout_option]

        self.security_menu.options = [self.security_on_option, self.security_off_option]

        self.landing_menu.options = [self.registration_menu, self.login_menu]

        self.account_settings_menu.options = [self.change_password_option, self.add_new_card_option, self.remove_card_option, self.landing_menu]

        self.user_list_menu.options = database_manager.get_user_list(account_manager, self.landing_menu)

        self.products_menu.options = [self.product1_menu, self.product2_menu, self.landing_menu]

    def guest_menu_options(self):
        """Sets landing menu options for non-users."""
        self.landing_menu.options = self.default_landing_options

    def user_menu_options(self):
        """Sets landing menu options for users."""
        self.landing_menu.options = self.user_landing_options

    def admin_menu_options(self):
        """Sets landing menu options for admins."""
        self.landing_menu.options = self.admin_landing_options
