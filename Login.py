from Handler import Handler
from Validation import Validation

class Login(Handler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = str(self.request.get("username"));
        password = str(self.request.get("password"));
        check = Validation()
        key = check.encrypt(username, password)

        if check.validate(username, password):
            self.response.headers.add_header('Set-Cookie', 'key=%s ; Path=/' %key)
            self.redirect('/notes')
        else:
            self.redirect('/login')





