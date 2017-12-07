import hashlib
import time
from psDB import Ps
from Handler import Handler

class Pw(Handler):
    def get(self):
        username = "jonathan"
        password = "jlcf1filsaime01"
        key = str(self.encrypt(username,password).hexdigest())

        self.write(key)

        db = Ps(ps = key)
        db.put()
        time.sleep(0.2)

        view = Ps.all()
        for k in view:
            self.write(k.ps)

    def encrypt(self, username, password ):
        return hashlib.sha256(username + password + username)