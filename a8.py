# Camden Hatch, Rasa Ichimori, Machael Backman, Jooyoung Jeon, Porter Rasmussen
# Section 4
# Description 

# Import random for generating random numbers
import random

import random

# These are all the classes:
# Order Class 
class Order (): 
    # Constructor
    def __init__(self):
    # Instance variable to store the number of burgers in the order
        self.burger_count = self.randomBurgers

    def randomBurgers (self):
        return random.randint(1, 20)


class Person:
    def __init__(self):
        self.customer_name = self.randomName()


    def randomName(self):
        lsCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        index = random.randint(0, len(lsCustomers) - 1)
        return lsCustomers[index]


# For loop:

    # Adding 100 customers into queue:

    # Customer's name as key in dictionary:



# Print list of customers and total burgers ordered sorted by most number of burgers:

