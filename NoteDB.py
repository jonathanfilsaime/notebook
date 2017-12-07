from google.appengine.ext import db

# database table for content
class Note(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    noteNumber = db.IntegerProperty()