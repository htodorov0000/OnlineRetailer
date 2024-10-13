"""Houses the Product module."""
from classes.menu_classes.numbered_menu import NavigationMenu

class Product(NavigationMenu):
    """Class for creating dummy Products with a price and 
    purchase option."""
    def __init__(self, name, description, account, price, buy, products_menu):
        name += " $" + str(price)
        description += " Price = $" + str(price)
        self.options = [buy, products_menu]
        super().__init__(name, description, account)
