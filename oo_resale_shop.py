class ResaleShop:
    from computer import Computer
    # Import the functions we wrote in procedural_resale_shop.py
    from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish
    # What attributes will it need?

    def printBanner():
        # Print a little banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    def buyComputer(computer):
        # Add it to the resale store's inventory
        print("Buying", computer.description)
        print("Adding to inventory...")
        computer_id = buy(computer)
        print("Done.\n")
        return computer_id

    def checkInventory():
         # Make sure it worked by checking inventory
        print("Checking inventory...")
        print_inventory()
        print("Done.\n")

    def refurbishComputer(computer, computer_id):
        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
        print("Updating inventory...")
        refurbish(computer_id, new_OS)
        print("Done.\n")

    def sellComputer(computer, computer_id):
        # Now, let's sell it!
        print("Selling Item ID:", computer_id)
        sell(computer_id)


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?