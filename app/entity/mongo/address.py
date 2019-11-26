import mongoengine

from app.CRUD.search.models import SearchableMixin


class Address(mongoengine.Document, SearchableMixin):
    __tablename__ = 'address_mongo'
    __searchable__ = ['detail']
    detail = mongoengine.StringField(max_length=60, required=True)
    district_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Address %r>' % (self.detail)
