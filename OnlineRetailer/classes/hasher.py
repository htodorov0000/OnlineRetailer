import hashlib
class Hasher:
    def hash(string, salt):
        string = string.encode("utf-8")
        hashed_string = hashlib.sha256(string + salt).hexdigest()
        return hashed_string
