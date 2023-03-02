from art import logo
import data

global_money = 0
current_drink = {
    "ingredients": {
        "water": 0,
        "milk": 0,
        "coffee": 0,
    },
    "cost": 0,
}


def print_report(remaining_res):
    print("Available resources:")
    print(f"Water: {remaining_res['water']}ml,")
    print(f"Milk: {remaining_res['milk']}ml,")
    print(f"Coffee: {remaining_res['coffee']}g,")
    print(f"Accumulated money: ${global_money}.")


def request_money(chosen_drink):
    money_sum = 0
    not_enough_money = True

    while not_enough_money:
        not_enough_money = False
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money_sum += 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

        if money_sum < chosen_drink['cost']:
            print(f"${money_sum} is not enough money! You need ${chosen_drink['cost']}. You can add some more: ")
            not_enough_money = True

    return money_sum


def check_choice(user_input, remaining_r):
    not_enough_res = False
    global current_drink

    if user_input == "espresso":
        drink = data.MENU['espresso']
        current_drink = drink
    elif user_input == "cappuccino":
        drink = data.MENU['cappuccino']
        current_drink = drink
    elif user_input == "latte":
        drink = data.MENU['latte']
        current_drink = drink
    elif user_input == "off":
        return 2
    elif user_input == "report":
        print_report(remaining_r)
        return 1
    else:
        print("Wrong choice, try again!")
        return -1

    if drink['ingredients']['water'] > remaining_r['water']:
        print("Sorry, there is not enough water!")
        not_enough_res = True
    if 'milk' in drink['ingredients']:
        if drink['ingredients']['milk'] > remaining_r['milk']:
            print("Sorry, there is not enough milk!")
            not_enough_res = True
    if drink['ingredients']['coffee'] > remaining_r['coffee']:
        print("Sorry, there is not enough coffee!")
        not_enough_res = True

    if not_enough_res:
        return 1
    else:
        remaining_r['water'] -= drink['ingredients']['water']
        remaining_r['milk'] -= drink['ingredients']['milk']
        remaining_r['coffee'] -= drink['ingredients']['coffee']
        return 0


def coffee_machine():
    global global_money
    print(logo)
    money_earned = 0
    remaining_res = data.resources
    continue_machine = True

    while continue_machine:
        print("==============================\n")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        feedback = check_choice(choice, remaining_res)
        print(current_drink)

        if feedback == 2:
            continue_machine = False
        elif feedback == 0:
            input_money = request_money(current_drink)
            money_earned += current_drink['cost']
            global_money = money_earned
            return_money = input_money - current_drink['cost']
            print(f"Here is your drink and ${return_money} change.\n")


coffee_machine()
