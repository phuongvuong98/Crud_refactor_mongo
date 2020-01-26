from mongoengine import *


class Category(Document):
    __tablename__ = 'category'

    name_vi = StringField(max_length=255, required=True)
    name_link = StringField(max_length=255, required=True)

    def __repr__(self):
        return '<Category %r>' % (self.name_link)
