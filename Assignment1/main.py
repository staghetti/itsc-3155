### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < quantity:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total_money = (large_dollars * 1 + (half_dollars * 0.5) + quarters * 0.25) + (nickels * 0.05)
        return total_money

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print(f"Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

# Instance
sandwich_machine = SandwichMachine(resources)

# Loop to keep machine running
while True:
    user_input = input("What would you like? (small/medium/large/off/report): ").lower() #case-insensitive

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


