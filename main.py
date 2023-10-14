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


def report_resources(current_resources, money_available):
    """Prints the current resource values"""
    for resource in current_resources:
        measurement = ""
        if resource == "Coffe":
            measurement = "g"
        else:
            measurement = "ml"
        print(f"{resource.title()}: {current_resources[resource]}{measurement}")
    print(f"Money: ${money_available}")


def check_resources(current_resources, chosen_menu_option):
    missing_resources = []
    for resource in current_resources:
        if resource in chosen_menu_option["ingredients"]:
            if current_resources[resource] < chosen_menu_option["ingredients"][resource]:
                missing_resources.append(resource)

    missing_resources_string = ""
    index = 0
    if len(missing_resources) > 0:
        for missing_resource in missing_resources:
            if len(missing_resources) == 1:
                missing_resources_string += missing_resource
            elif len(missing_resources) == 2 and index == 0:
                missing_resources_string += missing_resource + " "
            elif index == len(missing_resources) - 1:
                missing_resources_string += "and " + missing_resource
            else:
                missing_resources_string += missing_resource + ", "
            index += 1
    return missing_resources_string


user_input = ""
while user_input.lower() != "off":
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        # Print report
        report_resources(resources, money)
    elif user_input.lower() == "espresso" or user_input.lower() == "latte" or user_input.lower() == "cappuccino":
        chosen_option = MENU[user_input]
        # Check resources sufficient
        depleted_resources = check_resources(resources, chosen_option)
        if depleted_resources != "":
            print(f"Sorry there is not enough {depleted_resources}.")
        else:
            # Prompt the user to insert coins
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            # Calculate the monetary value of the coins inserted
            amount_given = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            change = round(amount_given - chosen_option["cost"], 2)
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            elif change >= 0:
                money += chosen_option["cost"]
                ingredients = chosen_option["ingredients"]
                for ingredient in ingredients:
                    resources[ingredient] -= ingredients[ingredient]
                if change > 0:
                    print(f"Here is ${change} in change")
                print(f"Here is your {user_input} Enjoy!")
