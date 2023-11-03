from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

restaurant_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String,
}

pizza_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'ingredients': fields.String,
}

class RestaurantResource(Resource):
    @marshal_with(restaurant_fields)
    def get(self):
        restaurants = Restaurant.query.all()
        return restaurants

class RestaurantByIdResource(Resource):
    @marshal_with(restaurant_fields)
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            return restaurant
        return {"error": "Restaurant not found"}, 404

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        return {"error": "Restaurant not found"}, 404

class PizzaResource(Resource):
    @marshal_with(pizza_fields)
    def get(self):
        pizzas = Pizza.query.all()
        return pizzas

class RestaurantPizzaResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True)
    parser.add_argument('pizza_id', type=int, required=True)
    parser.add_argument('restaurant_id', type=int, required=True)

    @marshal_with(pizza_fields)
    def post(self):
        data = self.parser.parse_args()
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        db.session.commit()
        return Pizza.query.get(pizza_id), 201

api.add_resource(RestaurantResource, '/restaurants/')
api.add_resource(RestaurantByIdResource, '/restaurants/<int:id>')
api.add_resource(PizzaResource, '/pizzas')
api.add_resource(RestaurantPizzaResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
