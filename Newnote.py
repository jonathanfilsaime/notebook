import time
from Validation import Validation
from Handler import Handler
from NoteDB import Note

class Newnote(Handler):
    def get(self):
        key = str(self.request.cookies.get('key'))
        check = Validation()

        if check.validateKey(key):
            self.response.headers.add_header('Set-Cookie', 'key=%s ; Path=/' %key)
            self.render("newnote.html")
        else:
            self.redirect('/login')



    def post(self):
        subject = self.request.get("subject")
        topic = self.request.get("topic")
        content = self.request.get("content")

        cancel = self.request.get("cancel")

        self.write(subject)
        self.write(topic)
        self.write(content)

        if cancel:
            self.redirect('/newnote')
        else:
            if subject and content:
                self.write("i got here")
                count = 1 + Note.all().count()
                note = Note(subject=subject, content=content, noteNumber= count)
                note.put()
                time.sleep(0.2)
                self.redirect('/notes')
            else:
                self.redirect('/newnote')



