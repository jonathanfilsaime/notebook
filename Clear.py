from psDB import Ps
from NoteDB import Note
from Handler import Handler

class Clear(Handler):
    def get(self):
        key = Ps.all()
        for k in key:
            k.delete()

        clef = Note.all()
        for c in clef:
            c.delete()

        self.write("all done")
