class AccountManager:
    def __init__(self):
        self.logged_in = False
        self.username = ""
        self.admin = False

    def set_menu_object_manager(self, menu_object_manager):
        self.menu_object_manager = menu_object_manager

    def login(self, username, admin):
        self.username = username
        self.admin = eval(admin.capitalize())
        self.logged_in = True
        if admin:
            self.menu_object_manager.admin_menu_options()
        else:
            self.menu_object_manager.user_menu_options()

    def log_out(self):
        self.username = ""
        self.admin = False
        self.logged_in = False
        self.menu_object_manager.guest_menu_options()
    
    def user_permissions(self):
        pass