import React, { useState, useEffect } from 'react';
import RestaurantPizza from './RestaurantPizza';
import './styles.css';


function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);
  const [showPizzas, setShowPizzas] = useState(false);

  useEffect(() => {
    fetch('/restaurants')
      .then((response) => response.json())
      .then((data) => setRestaurants(data));
  }, []);

  const deleteRestaurant = (id) => {
    fetch(`/restaurants/${id}`, {
      method: 'DELETE',
    }).then(() => {
      setRestaurants((prevRestaurants) =>
        prevRestaurants.filter((restaurant) => restaurant.id !== id)
      );
    });
  };

  const toggleShowPizzas = ()=>{
    setShowPizzas(!showPizzas)
  }

  return (
    <div className="restaurant-list">
      <table>
        <thead>
          <tr>
            <th>Restaurant Name</th>
            <th>Address</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {restaurants.map((restaurant) => (
            <tr key={restaurant.id}>
              <td>{restaurant.name}</td>
              <td>{restaurant.address}</td>
              <td>
                <button onClick={() => deleteRestaurant(restaurant.id)} className='delete'>Delete</button>
                <button onClick={toggleShowPizzas} className='available'>Available Pizzas</button>

              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {showPizzas && <RestaurantPizza/>}
    </div>
  );
}

export default RestaurantList;


