This project of writing in Django uses a different DDD (Domain-Driven Design) approach to separate business logic and application infrastructure.
This app implements the business logic of completing payment transactions and transferring encrypted data to the LiqPay payment gateway. In addition, you can also add an end point to remove payment information from the payment gateway
## Modules

### Customer
- Manages customer-related functionalities.
- Includes APIs for customer actions like viewing the menu and placing orders.

### Cart
- Handles the shopping cart functionalities.
- Allows adding, removing, and updating items in the cart.

### Menu
- Manages menu items.
- Provides APIs to retrieve and display menu items.

### Order
- Manages customer orders.
- Includes functionalities to create, update, and retrieve orders.

### Payment Callbacks
- Handles payment callback functionalities.
- Manages payment status updates and validations.

## Technologies Used
- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker

## Setup
1. Clone the repository.
2. Install dependencies using Poetry.
3. Set up the database.
4. Run the application using Docker.

## Testing
- Unit tests are provided for each module.
- Use `pytest` to run the tests.

## Contributing
- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request for review.
