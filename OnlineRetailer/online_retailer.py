INVALID_INPUT: str = "Invalid input. Try again."

class NumberedMenu:
    user_input: int
    def __init__(self, name, menu_items):
        self.name = name
        self.menu_items = menu_items

    def draw_menu(self):
        menu_string = ""
        for num, menu_item in enumerate(self.menu_items):
            menu_string += (str(num) + ". " + menu_item + """
""")
        while True:
            try:
                self.user_input = int(input(menu_string))
                if self.user_input < len(self.menu_items):
                    break
                else:
                    print(INVALID_INPUT)
            except:
                print("Please input a number in the correct range.")
        print(self.menu_items[self.user_input])
        

security_menu = NumberedMenu("Security Menu", ["Security ON", "Security OFF"])
security_menu.draw_menu()

# while True:
#     security_input = input("""1. Security On
# 2. Security Off
# """)
#     if security_input == "1":
#         security = True
#         print("Security mode ON")
#         break
#     if security_input == "2":
#         security = False
#         print("Security mode OFF")
#         break
#     print(INVALID_INPUT)

