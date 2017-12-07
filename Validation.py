import hashlib
from psDB import Ps

class Validation():
    def validate(self, username, password):
        key = Ps.all()
        val = ""

        for ps in key:
            val = ps.ps
        if self.encrypt(username, password)== val:
            return True
        else:
            return False

    def validateKey(self, key):
        check = Ps.all()
        val =""

        for ps in check:
            val = ps.ps
        if key == val:
            return True
        else:
            return False

    def encrypt(self, username, password ):
        return hashlib.sha256(username + password + username).hexdigest()
