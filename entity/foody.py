from mongoengine import *


class Foody(Document):
    __tablename__ = 'foody'

    name = StringField(max_length=255, required=True)
    link_foody = StringField(max_length=255)
    link_gg = StringField(max_length=500)
    min_price = LongField()
    max_price = LongField()
    address = StringField(max_length=255)
    system = StringField(max_length=60)
    categories = ListField()
    location = DictField()

    def __repr__(self):
        return '<Foody %r>' % (self.name)
