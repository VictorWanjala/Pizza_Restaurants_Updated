from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db,Restaurant,RestaurantPizza,Pizza
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#GET /restaurants

@app.route('/restaurants/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurants_data = [
        {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        for restaurant in restaurants
    ]
    return jsonify(restaurants_data)

# GET /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant_data={
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        return jsonify(restaurant_data)
    else:
        return jsonify({'error':'Restaurant not found'}, 404)
    
#DELETE/Restaurants/:id
@app.route('/restaurants/<int:id>',methods=['DELETE'])
def delete_restaurant(id):
    restaurant=Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return 'Restaurant deleted successfully!', 204
    else:
        return jsonify({'error':'Restaurant not found'}), 404
    
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_data = [{
        'id':pizza.id,
        'name':pizza.name,
        'ingredients': pizza.ingredients
    }for pizza in pizzas]
    return jsonify(pizza_data)

@app.route('/restaurant_pizzas', methods=['POST'])
def post_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({'errors':['price, pizza_id, and restaurant_id are required']}), 400
    
    restaurant_pizza = RestaurantPizza(price=price,pizza_id=pizza_id,restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()
    pizza = Pizza.query.get(pizza_id)
    return jsonify({
        'id':pizza.id,
        'name': pizza.name,
        'ingredients':pizza.ingredients
    }), 201
  
        

    





if __name__ == '__main__':
    app.run(port=5555)
    app.run(debug=True)