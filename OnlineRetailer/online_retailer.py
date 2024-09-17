from menu_classes import NumberedMenu
from menu_classes import SettingBoolMenu
from menu_classes import NavigationMenu
            
#Declare menu objects:

security_menu = SettingBoolMenu("Security Mode")     
landing_menu = NavigationMenu("Landing")
test_nav_menu2 = NavigationMenu("TestNavMenu2")
test_nav_menu3 = NavigationMenu("TestNavMenu3")
test_nav_menu4 = NavigationMenu("TestNavMenu4")

#Define menu paths:

security_menu.menu_items = ["Security ON", "Security OFF"]
landing_menu.menus = [test_nav_menu2, test_nav_menu3, test_nav_menu4]
# test_nav_menu2.menus = [test_nav_menu1, test_nav_menu3, test_nav_menu4]
# test_nav_menu3.menus = [test_nav_menu1, test_nav_menu2, test_nav_menu4]
# test_nav_menu4.menus = [test_nav_menu1, test_nav_menu2, test_nav_menu3]

#Security:
security_menu.start()
security = security_menu.setting

#TODO: Change settings depending on security here

#Start:
test_nav_menu1.start()
