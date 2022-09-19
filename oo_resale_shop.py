"""
DESCRIPTION
    The ResaleShop class contains methods for modifying the number of inventory 
    items in the shop and changing the attributes of computers in the inventory

ATTRIBUTES
    inventory - this is a dictionary where the key is an integer computer_id 
                used to access Computer objects  

METHODS 
   printBanner()
       prints a decorative banner
  
   buyComputer()
       adds a computer to the inventory
   
   checkInventory()
       prints details for everything in the inventory
   
   refurbishComputer()
       updates the price of the computer based on year created; updates OS if told to
   
   sellComputer()
       selfs computer if in the inventory and removes it from the inventory
   
   updatePrice()
       changes the price of the computer if found
"""

from typing import Dict 
from computer import Computer 

computer_id = 0
# What attributes will it need?
inventory : Dict[int, Computer] = {}

class ResaleShop:
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory : Dict):
        self.inventory = inventory 

    # What methods will you need?
    def printBanner():
        # Prints a little banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)
    
    def buyComputer(computer : Computer):
        # Adds a computer to resale store's inventory
        global computer_id
        computer_id += 1 #increment computer_id
        inventory[computer_id] = computer 
        return computer_id

    def checkInventory():
         # Prints all the items in the inventory 
         # if it is not empty
        if inventory:
        # For each item
            for computer_id in inventory:
            # Print its details
                print(f'computer_id: {computer_id} : {inventory[computer_id]}')
        else:
            print("No inventory to display.")

    def refurbishComputer(computer_id : int, new_OS : str):
        # Updates the price or operating system of 
        # a computer based on its age  
        if computer_id in inventory:
            computer = inventory[computer_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_OS is not None:
                computer["operating_system"] = new_OS # update details after installing new OS
        else:
            print("Item", computer_id, "not found. Please select another item to refurbish.")

    def sellComputer(computer : Computer , computer_id : int):
        # Sells a computer if it is in the inventory
        if computer_id in inventory:
            del inventory[computer_id]
            print("Item", computer_id, "sold!")
        else: 
            print("Item", computer_id, "not found. Please select another item to sell.")

    def updatePrice(computer_id : int, new_price : int):
        if computer_id in inventory:
            inventory[computer_id]["price"] = new_price
        else:
            print("Item", computer_id, "not found. Cannot update price.")
