"""This module houses the Hasher class."""
import hashlib
class Hasher:
    """For hashing data."""
    def hash(self, string, salt):
        """Hashes the given string using the given salt 
    and the SHA-256 algorithm and returns the hash."""
        string = string.encode("utf-8")
        hashed_string = hashlib.sha256(string + salt).hexdigest()
        return hashed_string
