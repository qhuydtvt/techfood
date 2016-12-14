from user import User
from mongoengine import *

class ToDo(Document):
    username = StringField()
    title = StringField()
    content = StringField()
    color = StringField()
