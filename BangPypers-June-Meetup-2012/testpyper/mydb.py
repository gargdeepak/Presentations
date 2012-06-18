
from google.appengine.ext import db

class PyperDB(db.Model):
    name = db.StringProperty(multiline=True);
    status = db.BooleanProperty();
    user_id = db.UserProperty();
    time = db.DateTimeProperty(auto_now_add=True);

