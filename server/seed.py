from app import db
from models import Restaurant, RestaurantPizza, Pizza
from faker import Faker
from app import app


fake = Faker()

with app.app_context():
    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    Pizza.query.delete()



    # Seed Restaurants
    print("Seeding restaurants...")
    restaurants_data = [
        {"name": "Sottocasa NYC", "address": "298 Atlantic Ave, Brooklyn, NY 11201"},
        {"name": "PizzArte", "address": "69 W 55th St, New York, NY 10019"},
        {"name": "Joe's Pizzeria", "address": "123 Main St, New York, NY 10001"},
        {"name": "Pizza Palace", "address": "456 Elm St, Brooklyn, NY 11202"},
        {"name": "Mama Mia's Pizzeria", "address": "789 Oak St, Queens, NY 11301"},
    
]
    
    for data in restaurants_data:
        restaurant = Restaurant(name=data["name"], address=data["address"])
        db.session.add(restaurant)

    db.session.commit()
    print("Done seeding restaurants.")

    # Seed Pizzas
    print("Seeding pizzas...")
    pizzas_data = [
        {"name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
        {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
        {"name": "Margherita", "ingredients": "Dough, Tomato Sauce, Mozzarella, Basil"},
        {"name": "Vegetarian", "ingredients": "Dough, Tomato Sauce, Cheese, Bell Peppers, Mushrooms, Olives"},
        {"name": "Hawaiian", "ingredients": "Dough, Tomato Sauce, Cheese, Ham, Pineapple"},
   
]


    for data in pizzas_data:
        pizza = Pizza(name=data["name"], ingredients=data["ingredients"])
        db.session.add(pizza)

    db.session.commit()
    print("Done seeding pizzas.")

    # Seed RestaurantPizzas
    print("Seeding restaurant pizzas...")
    restaurant_pizzas_data = [
        {"price": 10, "pizza_id": 1, "restaurant_id": 1},
        {"price": 12, "pizza_id": 2, "restaurant_id": 1},
        {"price": 9, "pizza_id": 1, "restaurant_id": 2},
        {"price": 11, "pizza_id": 2, "restaurant_id": 2},
    ]

    for data in restaurant_pizzas_data:
        restaurant_pizza = RestaurantPizza(
            price=data["price"], pizza_id=data["pizza_id"], restaurant_id=data["restaurant_id"]
        )
        db.session.add(restaurant_pizza)

    db.session.commit()
    print("Done seeding restaurant pizzas.")
