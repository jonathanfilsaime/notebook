from Handler import Handler
from NoteDB import Note

class Delete(Handler):
    def get(self):
        all = Note.all()

        for p in all:
            p.delete()
