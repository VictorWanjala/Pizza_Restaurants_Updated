import React, { useState, useEffect } from 'react';
import './styles.css';


function RestaurantPizza() {
  const [pizzas, setPizzas] = useState([]);
  const [showPizzas, setShowPizzas] = useState(false); 
  const [newPizza, setNewPizza] = useState({ price: 0, pizza_id: 0, restaurant_id: 0 });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewPizza((prevPizza) => ({
      ...prevPizza,
      [name]: value,
    }));
  };

  const postRestaurantPizza = () => {
    const priceAsInt = parseInt(newPizza.price, 10);
    const pizzaData = {...newPizza, price: priceAsInt};
    fetch('/restaurant_pizzas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(pizzaData),
    })
      .then((response) => response.json())
      .then((data) => {
        setPizzas((prevPizzas) => [...prevPizzas, data]);
      })
      .catch((error) => {
        console.error('Error posting restaurant pizza:', error);
      });
  };

  useEffect(() => {
    fetch('/pizzas')
      .then((response) => response.json())
      .then((data) => setPizzas(data));
  }, []);

  const togglePizzas = () => {
    setShowPizzas(!showPizzas);
  };

  return (
    <div className="restaurant-pizza">
      <h2>Available Pizzas</h2>
      <button onClick={togglePizzas}>
        {showPizzas ? 'Hide Pizzas' : 'Show Pizzas'}
      </button>

      {showPizzas && (
        <table>
          <thead>
            <tr>
              <th>Pizza Name</th>
              <th>Ingredients</th>
            </tr>
          </thead>
          <tbody>
            {pizzas.map((pizza) => (
              <tr key={pizza.id}>
                <td>{pizza.name}</td>
                <td>{pizza.ingredients}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <h2>Add a Pizza</h2>
      <div>
        <label>
          Price:
          <input
            type="number"
            name="price"
            value={newPizza.price}
            onChange={handleInputChange}
          />
        </label>
      </div>
      <div>
        <label>
          Pizza ID:
          <input
            type="number"
            name="pizza_id"
            value={newPizza.pizza_id}
            onChange={handleInputChange}
          />
        </label>
      </div>
      <div>
        <label>
          Restaurant ID:
          <input
            type="number"
            name="restaurant_id"
            value={newPizza.restaurant_id}
            onChange={handleInputChange}
          />
        </label>
      </div>
      <button onClick={postRestaurantPizza}>Add Pizza</button>
    </div>
  );
}

export default RestaurantPizza;

