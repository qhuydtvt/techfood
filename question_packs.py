__author__ = 'qhuydtvt'

from mongoengine import *
from versions import Version

class QuestionPack(Document):
    available_time = StringField()
    question_ids = ListField(StringField())
    level = IntField()

class QuestionPackCollection(Document):
    question_packs = ListField(EmbeddedDocumentField('QuestionPack'))

