from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)


class BlogPost(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateProperty(auto_now_add=True)
    last_modified = db.DateProperty(auto_now=True)