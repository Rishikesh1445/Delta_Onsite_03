from . import db
from flask_login import UserMixin

class items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    ownership = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    sell = db.Column(db.Boolean, default = False)

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price
        }


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
