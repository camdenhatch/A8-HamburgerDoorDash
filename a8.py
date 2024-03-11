# Camden Hatch, Rasa Ichimori, Machael Backman, Jooyoung Jeon, Porter Rasmussen
# Section 4

import random

# These are all the classes:

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

