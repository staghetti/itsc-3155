import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    ###  write the rest of the codes ###
    # Loop to keep machine running
    while True:
        user_input = input("What would you like? (small/medium/large/off/report): ").lower()  # case-insensitive

        # User input to turn off the machine
        if user_input == "off":
            print("Machine off...Goodbye!")
            break
        # Report of current resources
        elif user_input == "report":
            # Listed resources displayed along with their current values
            for ingredient, quantity in sandwich_machine.machine_resources.items():
                unit = 'slice(s)' if 'bread' in ingredient or 'ham' in ingredient else 'pound(s)'
                print(f"{ingredient.capitalize()}: {quantity} {unit}")
        # Process the user's order and inserted coins
        elif user_input in recipes:
            # Determining size and ingredients
            order_size = user_input
            order_ingredients = recipes[order_size]["ingredients"]

            # Checking whether there are enough resources to make the sandwich
            if sandwich_machine.check_resources(order_ingredients):
                print("Please insert coins.")
                coins_inserted = sandwich_machine.process_coins()
                order_cost = recipes[order_size]["cost"]

                # Checking if transaction is successful and if change needs to be distributed
                if sandwich_machine.transaction_result(coins_inserted, order_cost):
                    sandwich_machine.make_sandwich(order_size, order_ingredients)
            else:
                # Invalid input
                print("")

if __name__=="__main__":
    main()