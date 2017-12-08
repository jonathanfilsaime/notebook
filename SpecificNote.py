import time
from Handler import Handler
from google.appengine.ext import db

class SpecificNote(Handler):
    def get(self, noteID=""):
        note = db.GqlQuery("SELECT * FROM Note WHERE noteNumber = " + str(noteID))
        self.render("newnote.html", note=note)

    def post(self, noteID=""):
        update =self.request.get("update")
        cancel =self.request.get("cancel")
        subject = self.request.get("subject")
        content = self.request.get("content")

        if update and subject != "" and content != "":
            note = db.GqlQuery("SELECT * FROM Note WHERE noteNumber = " + str(noteID))
            for entry in note:
                entry.subject = subject
                entry.content = content
                entry.put()

            time.sleep(0.2)
            self.redirect('/notes')

        if cancel:
            self.redirect('/notes')

        if subject == "" and content == "" and update :
            note = db.GqlQuery("SELECT * FROM Note WHERE noteNumber = " + str(noteID))
            for entry in note:
                entry.delete()

            time.sleep(0.2)
            self.redirect('/notes')

