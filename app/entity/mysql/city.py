from app import db


class City(db.Model):
    __tablename__ = 'city'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    # district = db.relationship(
    #     "District", backref='city', lazy="dynamic")

    def __repr__(self):
        return '<City %r>' % self.name
