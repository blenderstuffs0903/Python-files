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

money = 0

# TODO: Print report.☑
# TODO: Check resources sufficient?☑
# TODO: Process coins.☑
# TODO: Check transaction successful?
# TODO: Make Coffee


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


def process_coins():
    print('Please insert coins.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def fill_up():
    global money
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    money = 0


is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice.lower() == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
    elif choice.lower() == 'off':
        print('Program Closed...')
        is_on = False
    elif choice == 'fillup':
        fill_up()

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if payment < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f'Here is your {choice}, enjoy.')
                if payment > drink['cost']:
                    change = round(payment-drink['cost'], 2)
                    print(f'Here is ${change} dollars in change.')
                money += drink['cost']
                for item in resources:
                    resources[item] -= drink['ingredients'][item]
