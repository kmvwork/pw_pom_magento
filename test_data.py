import random

number = random.randint(1, 100000)

account_creation_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": f"{number}john.doe@example.com",
    "password": "password123!",
    "confirm_password": "password123!",
}

expected_titles = {
    "account_creation": "Create New Customer Account",
    "eco_friendly": "Eco Friendly",
    "sale": "Sale",
}
