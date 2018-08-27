# HBNB RESTful API

This module contains the code for HBNB's API.


## Requests

HBNB's API supports various HTTP requests. Here's a basic example to check the status of the API. It assumes that the API is running on the local machine at port 5000.
```
$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
```
This is a GET request to the '/status' route. Here's a full list of available routes and request methods:

### Misc

* GET /api/v1/status - returns status of API

### States
* GET /api/v1/states - returns list of all states in database
* POST /api/v1/states - creates a new state
  * must contain 'name' attribute. Example:
```
$ curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}'
{
  "__class__": "State",
  "created_at": "2017-04-15T01:30:27.557877",
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6",
  "name": "California",
  "updated_at": "2017-04-15T01:30:27.558081"
}
```
* GET /api/v1/states/<state_id> - retrieves a state
* DELETE /api/v1/states/<state_id> - deletes a state
* PUT /api/v1/states/<state_id> - updates a state

### Cities
* GET /api/v1/states/<state_id>/cities - returns list of all cities in a state
* POST /api/v1/states/<state_id>/cities - creates a new city
  * must contain 'name' attribute
* GET /api/v1/cities/<city_id> - retrieves a city
* DELETE /api/v1/cities/<city_id> - deletes a city
* PUT /api/v1/cities/<city_id> - updates a city

### Amenities
* GET /api/v1/amenities - returns list of all amenities
* POST /api/v1/amenities - creates a new amenity
  * must contain 'name' attribute
* GET /api/v1/amenities/<amenity_id> - retrieves an amenity
* DELETE /api/v1/amenities/<amenity_id> - deletes an amenity
* PUT /api/v1/amenities/<amenity_id> - updates an amenity

### Users
* GET /api/v1/users - returns list of all users
* POST /api/v1/users - creates a new user
  * must contain 'email' and 'password' attributes
* GET /api/v1/users/<user_id> - retrieves a user
* DELETE /api/v1/users/<user_id> - deletes a user
* PUT /api/v1/users/<user_id> - updates a user

### Places
* GET /api/v1/cities/<city_id>/places - returns list of all places in a city
* POST /api/v1/cites/<city_id>/places - creates a new place
  * must contain 'user_id' and 'name' attributes
* GET /api/v1/places/<place_id> - retrieves a place
* DELETE /api/v1/places/<place_id> - deletes a place
* PUT /api/v1/places/<place_id> - updates a place

### Reviews
* GET /api/v1/places/<place_id>/reviews - returns list of all place of a place
* POST /api/v1/places/<place_id>/reviews - creates a new review
  * must contain 'user_id' attribute
* GET /api/v1/reviews/<review_id> - retrieves a review
* DELETE /api/v1/reviews/<review_id> - deletes a review
* PUT /api/v1/reviews/<review_id> - updates a review

### Places/Amenities
* GET /api/v1/places/<place_id>/amenities - returns list of all amenities in a place
* DELETE /api/v1/places/<place_id>/amenities/<amenity_id> - deletes an amenity from a place
* POST /api/v1/places/<place_id>/amenities/<amenity_id> - links an amenity to a place

### Places Search
* POST /api/v1/api/v1/places_search - searches for places in a set of locations, featuring a set of amenities.
  * can, but does not have to, contain 'states', 'cities', and 'amenities' attribute. Example:
```
$ curl -X POST http://0.0.0.0:5000/api/v1/places_search -H "Content-Type: application/json" -d '{"states": ["2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", "459e021a-e794-447d-9dd2-e03b7963f7d2"], "cities": ["5976f0e7-5c5f-4949-aae0-90d68fd239c0"], "amenities": []}'
[
  {
   "__class__": "Place",
   "created_at": "2017-03-25T02:17:06",
   "id": "dacec983-cec4-4f68-bd7f-af9068a305f5",
   "name": "The Lynn House",
   "city_id": "1721b75c-e0b2-46ae-8dd2-f86b62fb46e6,
   "user_id": "3ea61b06-e22a-459b-bb96-d900fb8f843a",
   "description": "Our place is 2 blocks from Vista Park (Farmer's Market), Historic Warren Ballpark, and about 2 miles from Old Bisbee where there is shopping, dining, and site seeing. We offer continental breakfast. You get the quiet life with great mountain and garden views. This is a 100+ year old cozy home which has been on both the Garden and Home tours. You have access to whole house, except for 1 restricted area (She-Shack).  Hosts are on site in a casita in the back from 8pm until 7am when we are in town.<BR /><BR />Our home has two bedrooms, one king and one queen.  There are 2 bathrooms, 1  1950's soak tub with shower and 1 with shower only.  Guests have access to the living/dining room area, and the kitchen (except for use of stove/oven).  Each morning, coffee/tea, and muffins are ready for guests.  A small frig is available in the dining room with water/juice and an area for guest items.  1 parking space is directly across the street.",
   "number_rooms": 2,
   "number_bathrooms": 2,
   "max_guest": 4,
   "price_by_night": 82,
   "latitude": 31.4141,
   "longitude": -109.879,
   "updated_at": "2017-03-25T02:17:06"
  },
}
```

## Documentation
Some Documentation is available at the /apidocs route. At the time of writing this, the documentation is not finished.
