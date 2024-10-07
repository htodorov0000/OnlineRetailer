from classes.account_manager import AccountManager
from classes.database_manager import DatabaseManager
from classes.menu_object_manager import MenuObjectManager

account_manager = AccountManager()
database_manager = DatabaseManager()
menu_object_manager = MenuObjectManager(account_manager, database_manager)
account_manager.set_menu_object_manager(menu_object_manager)


#TODO: Change settings depending on security and login here

#Security:
menu_object_manager.security_menu.start()
menu_object_manager.security = menu_object_manager.security_menu.setting

#Start:
menu_object_manager.landing_menu.start()
