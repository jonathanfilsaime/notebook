from google.appengine.ext import db

# database table for content
class Ps(db.Model):
    ps = db.StringProperty(required = True)