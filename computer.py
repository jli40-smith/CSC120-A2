# What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
class Computer:
    #Constructor sets up the class Computer
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

x = Computer("MacBook Pro","Intel", 256, 16,"Mac OS", 2017, 1999)

print(x.description, x.processor_type, x.hard_drive, x.memory, x.operating_system, x.year_made, x.price)
    # What methods will you need?