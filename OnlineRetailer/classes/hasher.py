import hashlib
import os
class Hasher:
    def hash(string):
        string = string.encode("utf-8")
        salt = os.urandom(32)
        hashed_string = hashlib.sha256(string + salt).hexdigest()
        return hashed_string
