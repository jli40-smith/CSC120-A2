"""The ResaleShop class contains methods for modifying the number of inventory 
items in the shop and changing the attributes of computers in the inventory
"""

class ResaleShop:

    # Import the functions we wrote in procedural_resale_shop.py
    from procedural_resale_shop import buy, print_inventory, refurbish, sell, update_price
    
    # What attributes will it need?
    inventory: dict

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory 
    # You'll remove this when you fill out your constructor

    # What methods will you need?
    def printBanner():
        # Prints a little banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    def buyComputer(computer):
        # Adds a computer to resale store's inventory
        print("Buying", computer.description)
        print("Adding to inventory...")
        computer_id = buy(computer)
        print("Done.\n")
        return computer_id

    def checkInventory():
         # Prints all the items in the inventory 
         # if it is not empty
        print("Checking inventory...")
        print_inventory()
        print("Done.\n")

    def refurbishComputer(computer, computer_id):
        # Updates the price or operating system of 
        # a computer based on its age  
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", computer_id,", updating OS to", new_OS)
        print("Updating inventory...")
        refurbish(computer_id, new_OS)
        print("Done.\n")

    def sellComputer(computer, computer_id):
        # Sells a computer if it is in the inventory 
        print("Selling Item ID:", computer_id)
        sell(computer_id)

    def updatePrice(computer, computer_id, new_price):
        #Changes the price of a computer to new_price
        print("Updating price of Item ID:", computer_id,"to", new_price)
        update_price(computer_id, new_price)