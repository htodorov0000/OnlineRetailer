from menu_classes import SettingBoolMenu
from menu_classes import NavigationMenu

DEFAULT_DESCRIPTION = "Please select the desired menu."

#Declare menu objects:

security_menu = SettingBoolMenu("Security Mode", "Please select the desired security setting.")     
landing_menu = NavigationMenu("Landing", DEFAULT_DESCRIPTION)

#Define menu paths:

security_menu.menu_items = ["Security ON", "Security OFF"]
landing_menu.options = [security_menu]


#Security:
security_menu.start()
security = security_menu.setting

#TODO: Change settings depending on security here

#Start:
landing_menu.start()
