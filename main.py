# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py

# Import Computer class from computer.py
from computer import Computer

# Import ResaleShop class from oo_resale_shop
from oo_resale_shop import ResaleShop


def main():
    
    # First, let's make a computer
    computer = Computer.create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Prints a little banner
    ResaleShop.printBanner()

    # Adds computer to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = ResaleShop.buyComputer(computer)
    print("Done.\n")
    
    # Prints inventory to make sure computer was added
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.checkInventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    ResaleShop.refurbishComputer(computer_id, new_OS)
    print("Done.\n")

# Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.checkInventory()
    print("Done.\n")

# Now, let's sell it!
    print("Selling Item ID:", computer_id)
    ResaleShop.sellComputer(computer, computer_id)

    # Prints inventory to make sure computer was added
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.checkInventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()