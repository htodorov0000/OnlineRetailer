import os
import unittest
from classes.hasher import Hasher
from classes.menu_classes.text_input_menu import AddCardMenu, RegistrationMenu

class SecurityManagerForTest():
        pass
class DatabaseManagerForTest():
    def is_username_taken(self, username):
        return False

class TestRegistrationMenu(unittest.TestCase):
    security_manager = SecurityManagerForTest()
    database_manager = DatabaseManagerForTest()
    def test_input_restriction(self):
        reg_menu = RegistrationMenu("Registration Menu", "", None, ["Username", "Password"], self.database_manager, None, self.security_manager,None)
        self.security_manager.security = True
        self.assertTrue(reg_menu.username_input_restriction("User12345"))
        self.assertFalse(reg_menu.username_input_restriction("User1"))
        self.assertFalse(reg_menu.username_input_restriction("=10+10"))
        
        self.assertTrue(reg_menu.password_input_restriction("Pas$w0rd12345"))
        self.assertFalse(reg_menu.password_input_restriction("pas$w0rd12345"))
        self.assertFalse(reg_menu.password_input_restriction("1"))

        self.security_manager.security = False
        self.assertTrue(reg_menu.username_input_restriction("User12345"))
        self.assertFalse(reg_menu.username_input_restriction("User1"))
        self.assertTrue(reg_menu.username_input_restriction("=10+10"))
        
        self.assertTrue(reg_menu.password_input_restriction("Pas$w0rd12345"))
        self.assertTrue(reg_menu.password_input_restriction("pas$w0rd12345"))
        self.assertTrue(reg_menu.password_input_restriction("1"))
        
class TestAddCardMenu(unittest.TestCase):
    def test_input_restriction(self):
        add_card = AddCardMenu("", "", None, None, None, None, None, None)
         
        self.assertTrue(add_card.name_restriction("John"))
        self.assertTrue(add_card.name_restriction("john"))
        self.assertFalse(add_card.name_restriction("john1"))
        self.assertFalse(add_card.name_restriction("johnjohnjohnjohnjohnjohnjohnjohnjohnjohnjohn"))
        
        self.assertTrue(add_card.card_number_restriction("1234123412341234"))
        self.assertFalse(add_card.card_number_restriction("abcdabcdabcdabcd"))
        self.assertFalse(add_card.card_number_restriction("12345123412341234"))
        
        self.assertTrue(add_card.cvc_restriction("123"))
        self.assertFalse(add_card.cvc_restriction("1.3"))
        self.assertFalse(add_card.cvc_restriction("one"))
        
class TestHasher(unittest.TestCase):
     def test_hash(self):
         hasher = Hasher()
         salt = "b'\xbdF\x07/\xdaC\xbde\xa4\xaf\xeac\xd5d5\x1d\xcer\xe1\x86x\xb1\xf9\x14\x1c\x88\x7fg\x1e\xb0\xb7\xa4".encode("utf-8")
         self.assertEqual(hasher.hash("Pas$w0rd1919", salt), hasher.hash("Pas$w0rd1919", salt))
         self.assertEqual(hasher.hash("Pas$w0rd1919", salt), "a")
                
if __name__ == "__main__":
    unittest.main()