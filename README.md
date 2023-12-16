# Object Relations Code Challenge - Restaurants

Welcome to the Object Relations Code Challenge for Restaurants! In this project, we'll be working with a Yelp-style domain consisting of three models: `Restaurant`, `Customer`, and `Review`. These models have specific relationships, and your task is to implement various methods to manage and analyze the data.

## Setup

1. Use the provided Pipfile to install all dependencies required for this project.

```bash
pipenv install
```
2. Create your own test sample instances to validate your code. Make sure to establish relationships and test your methods in the console before submitting.

## Getting Started

Before diving into coding, I am to draw the domain on paper or a whiteboard to identify a single source of truth for your data. This will help design classes and relationships more effectively.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- Lists and List Methods

## Deliverables

### `Initializers, Readers, and Writers`

#### Customer

- `Customer __init__(given_name, family_name)`

    Initializes a customer with a given name and family name.
- `Customer given_name()`

    Returns the customer's given name.
- `Customer family_name()`

    Returns the customer's family name.
- `Customer full_name()`

    Returns the full name of the customer, Western style.
- `Customer all()`

    Returns all customer instances.

#### Restaurant

- `Restaurant __init__(name)`

    Initializes a restaurant with a name.
- `Restaurant name()`

    Returns the restaurant's name.

#### Review

- `Review __init__(customer, restaurant, rating)`

    Initializes a review with a customer, restaurant, and rating.
- `Review rating()`

    Returns the rating for a restaurant.
- `Review all()`

    Returns all reviews.

### `Object Relationship Methods`

#### Review
- `Review customer()`

    Returns the customer object for that review.
- `Review restaurant()`

    Returns the restaurant object for that given review.

#### Restaurant
- `Restaurant reviews()`

    Returns a list of all reviews for that restaurant.
- `Restaurant customers()`

    Returns a unique list of all customers who have reviewed the restaurant.
#### Customer
- `Customer restaurants()`

    Returns a unique list of all restaurants a customer has reviewed.
- `Customer add_review(restaurant, rating)`

    Creates a new review and associates it with the customer and restaurant.

### `Aggregate and Association Methods`

#### Customer
- `Customer num_reviews()`

    - Returns the total number of reviews that a customer has authored.
- `Customer find_by_name(name) (class method)`

    - Returns the first customer whose full name matches the given string.
- `Customer find_all_by_given_name(name) (class method)`

    - Returns a list containing all customers with the given name.

#### Restaurant

- `Restaurant average_star_rating()`
    
    - Returns the average star rating for a restaurant based on its reviews.

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

### Author

- David Munuhe Muchoki