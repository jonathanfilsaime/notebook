import json
from Handler import Handler
from NoteDB import Note
from Validation import Validation

class Notes(Handler):
    def get(self):
        key = str(self.request.cookies.get('key'))
        check = Validation()

        if check.validateKey(key):
            self.response.headers.add_header('Set-Cookie', 'name=%s ; Path=/' %key)
            allNotes = Note.all()
            allNotes.order('-created')

            # notesDictionary = []
            # for note in allNotes:
            #     noteDic = {
            #         'subject' : note.subject,
            #         'date': str(note.created.date()),
            #         'content' : note.content,
            #     }
            #     notesDictionary.append(noteDic)
            #
            # self.response.write(json.dumps(notesDictionary))

            self.render("notes.html", allNotes=allNotes)
        else:
            self.redirect('/login')


