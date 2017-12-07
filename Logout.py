from Handler import Handler

class Logout(Handler):
    def get(self):
        self.response.headers.add_header('Set-Cookie', 'key= ; Path=/'  )
        self.redirect('/login')