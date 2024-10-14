"""Main module, run this file to start the program."""

from classes.data_managers.account_manager import AccountManager
from classes.data_managers.database_manager import DatabaseManager
from classes.data_managers.menu_object_manager import MenuObjectManager
from classes.data_managers.security_manager import SecurityManager

#Create objects for data management:
account_manager = AccountManager()
database_manager = DatabaseManager()
security_manager = SecurityManager(database_manager)
menu_object_manager = MenuObjectManager(account_manager, database_manager, security_manager)
account_manager.set_menu_object_manager(menu_object_manager)

#Security:
menu_object_manager.security_menu.start()

#Start:
menu_object_manager.landing_menu.start()
