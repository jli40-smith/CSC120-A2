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
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.checkInventory()
    print("Done.\n")

    #Changes price of computer to 1000
    ResaleShop.updatePrice(computer_id, 1000)

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
    
    #Testing error messages
    print("Selling Item ID:", computer_id)
    ResaleShop.sellComputer(computer, computer_id)

        #Changes price of computer to 1000
    ResaleShop.updatePrice(computer_id, 1000)

    ResaleShop.refurbishComputer(computer_id, new_OS)



# Calls the main() function when this file is run
if __name__ == "__main__": main()