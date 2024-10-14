"""This module houses the SecurityManager class."""
class SecurityManager:
    """Sets the security mode based on initial question and
    tracks it."""
    def __init__(self, database_manager):
        self.security = False
        self.database_manager = database_manager

    def set_security_mode(self, security):
        """Sets security boolean variable for later tracking and 
        the database CSV file used by the DatabaseManager."""
        self.security = security
        if security:
            self.database_manager.database = "database/account_data_secure.csv"
        else:
            self.database_manager.database = "database/account_data_insecure.csv"
