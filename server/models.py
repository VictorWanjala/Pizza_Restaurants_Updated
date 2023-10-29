from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates



db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'Restaurant')

    def __init__(self, name,address):
        self.name=name
        self.address = address



class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    @validates('price')
    def validate_price(self, key, value):
        if not(1<= value <=30):
            raise ValueError('Price must be between 1 and 30.')
        return value

    def __init__(self, price,restaurant_id, pizza_id):
        self.price=price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'Pizza')
    def __init__(self, name,ingredients):
        self.name=name
        self.ingredients = ingredients








