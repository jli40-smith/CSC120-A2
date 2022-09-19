"""
DESCRIPTION
    Holds details about the computers  
    of the resale shop inventory 

ATTRIBUTES 
    description 
        string containing name of the computer 
    
    processor_type 
        string containing name of computer's processor  
    
    hard_drive_capacity 
        integer with amount of hard drive capacity 
    
    memory
        integer with amount of memory in computer 
   
    operating_system 
        string representing the operating system of computer 
    
    year_made 
        integer representing year computer was manufactured 
    price
        integar representing cost of computer 

METHODS 
    create_computer() - packages the attributes in computer into a dictionary 
"""
class Computer:

    # ATTRIBUTES: info about pretty much all computers!
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # CONSTRUCTOR: make the computer!
    def __init__(self, description, processor_type, 
                hard_drive_capacity, memory, operating_system,
                year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # METHODS: function to create a computer! (helpful for refurbishing)
    def create_computer(description: str,
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
                }