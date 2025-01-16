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

COINS_ACCEPTED = {
    "quarters": {
        "quantity": 0,
        "value": 0.25,
    },
    "dimes": {
        "quantity": 0,
        "value": 0.1,
    },
    "nickles": {
        "quantity": 0,
        "value": 0.05,
    },
    "pennies": {
        "quantity": 0,
        "value": 0.01,
    },
}

should_continue = True

def print_report():
    for r in resources:
        if r == "coffee":
            print(f"{r.title()}: {resources[r]}g")
        elif r == "money":
            print(f"{r.title()}: ${resources[r]}")
        else:
            print(f"{r.title()}: {resources[r]}ml")

def check_resources(choice):
    recipe = MENU[choice]
    for i in recipe["ingredients"]:
        if resources[i] < recipe["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            break

def process_coins():
    coins = COINS_ACCEPTED
    total_inserted = 0
    print("Please insert coins.")

    for key in coins:
        coins[key]["quantity"] = int(input(f"How many {key}?: "))
        total_inserted += coins[key]["quantity"] * coins[key]["value"]
        print(f"Inserted {coins[key]['quantity']} {key}. " +
              f"Total Inserted: {coins[key]['quantity'] * coins[key]['value']}. " +
              f"Total accumulated: {total_inserted}")

    return round(total_inserted, 2)

def check_transaction(value, choice):
    print(f"value: {value}, choice: {choice}, cost: {MENU[choice]['cost']}")
    print(f"Types -> value: {type(value)}, choice: {type(choice)}, cost: {type(MENU[choice]['cost'])}")

    if value < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if value > MENU[choice]["cost"]:
            change = round(value - MENU[choice]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
        return True

def make_coffe(choice):
    recipe = MENU[choice]
    for i in recipe["ingredients"]:
        resources[i] -= recipe["ingredients"][i]
    print_report()
    print(f"Here's your {choice}. Enjoy!")

while should_continue:

    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        should_continue = False
    elif order == "report":
        print_report()
    else:
        check_resources(order)
        value_inserted = process_coins()
        if check_transaction(value_inserted, order):
            make_coffe(order)
