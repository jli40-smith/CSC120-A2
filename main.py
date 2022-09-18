# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

# Import Computer class from computer.py
from computer import Computer

# Import ResaleShop class from oo_resale_shop
from oo_resale_shop import ResaleShop

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
"""def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }"""

def main():
    
    # First, let's make a computer
    computer = Computer.create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Prints a computer shop banner
    ResaleShop.printBanner()

    # Adds computer to the resale store's inventory
    computer_id = ResaleShop.buyComputer(computer)

    # Prints inventory to make sure computer was added
    ResaleShop.checkInventory()

    #Changes the price of the computer 
    ResaleShop.updatePrice(computer_id, 1000)

    # Prints inventory to make sure price of computer changed
    ResaleShop.checkInventory()

    # Refurbishes computer to update OS and update change to inventory
    ResaleShop.refurbishComputer(computer_id)

    # Checks inventory to make sure computer was refurbished
    ResaleShop.checkInventory()
    
    # Sells the computer
    ResaleShop.sellComputer(computer, computer_id)
    
    # Checks inventory to make sure computer was sold
    ResaleShop.checkInventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()
