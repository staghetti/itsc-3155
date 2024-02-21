class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total_money = (large_dollars * 1 + (half_dollars * 0.5) + quarters * 0.25) + (nickels * 0.05)
        return total_money

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print(f"Sorry, that's not enough money. Money refunded.")
            return False