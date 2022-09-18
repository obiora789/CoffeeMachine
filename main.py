MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01
income = 0


def restock_resources():
    """Restocks resources"""
    resources["water"] += 1200
    resources["milk"] += 600
    resources["coffee"] += 300


def resources_sufficient(user_input):
    """Compares the resources remaining to the resources required to serve the next user and returns a boolean."""
    water_required = MENU[user_input]["ingredients"]["water"]
    coffee_required = MENU[user_input]["ingredients"]["coffee"]
    if resources["water"] < water_required:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < coffee_required:
        print("Sorry there is not enough coffee.")
        return False
    if user_input == "cappuccino" or user_input == "latte":
        milk_required = MENU[user_input]["ingredients"]["milk"]
        if resources["milk"] < milk_required:
            print("Sorry there is not enough milk.")
            return False
    return True


def give_change(user_input, total_sum, coffee_cost):
    """Processes the change remaining after deducting cost or refunds the user if money is incomplete."""
    emoji = "☕️"
    water_required = MENU[user_input]["ingredients"]["water"]
    coffee_required = MENU[user_input]["ingredients"]["coffee"]
    if total_sum > coffee_cost:
        change_remaining = total_sum - coffee_cost
        resources["water"] -= water_required
        resources["coffee"] -= coffee_required
        resources["money"] += coffee_cost
        if user_input == "latte" or user_input == "cappuccino":
            milk_required = MENU[user_input]["ingredients"]["milk"]
            resources["milk"] -= milk_required
        change_remaining = round(change_remaining, 2)
        change_left = "{:.2f}".format(change_remaining)
        print(f"Here is ${change_left} in change.")
        print(f"Here is your {user_input} {emoji}. Enjoy!")
        return change_remaining
    elif total_sum < coffee_cost:
        print("Sorry you don't have enough money. Money refunded")
        return -1
    else:
        print(f"Here is your {user_input} {emoji}. Enjoy!")
        return 0


def calculate_money(user_input):
    """Calculates the whole money put into the coin deposit and returns the change."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * QUARTER
    dimes = int(input("How many dimes? ")) * DIME
    nickels = int(input("How many nickels? ")) * NICKEL
    pennies = int(input("How many pennies? ")) * PENNY
    cost = MENU[user_input]["cost"]
    total = pennies + nickels + dimes + quarters
    change_remaining = give_change(user_input, total, cost)
    return change_remaining


user_choice = input("What would you like? (espresso/latte/cappuccino): ")
off = False
resources["money"] = income
while not off:
    change = 0
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']}")
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    elif user_choice == "restock":
        restock_resources()
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    elif user_choice == "off":
        print("GoodBye!")
        off = True
    else:
        if resources_sufficient(user_choice):
            change = calculate_money(user_choice)
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
