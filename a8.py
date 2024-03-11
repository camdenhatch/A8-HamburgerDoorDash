# Camden Hatch, Rasa Ichimori, Machael Backman, Jooyoung Jeon, Porter Rasmussen
# Section 4
# This program tracks exactly how many hamburgers each customer eats.  

# Import random for generating random numbers
import random

# Order Class 
class Order (): 
    # Constructor
    def __init__(self):
    # Instance variable to store the number of burgers in the order
        self.burger_count = self.randomBurgers

    # Method that returns a number between 1 and 20
    def randomBurgers (self):
        return random.randint(1, 20)

# Person Class
class Person:
    # Constructor
    def __init__(self):
    # Instance variable called customer_name
        self.customer_name = self.randomName()

    # Method that contains a list of 9 names
    def randomName(self):
        lsCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", \
                       "Invisible Swordsman", "Singing Bush"]
        # Randomly returns one of the 9 names when called
        index = random.randint(0, len(lsCustomers) - 1)
        return lsCustomers[index]


# Customer Class 
class Customer (Person): 
    # Constructor class that inherits from parent Person class
    def __init__(self):
        super().__init__()
    # Instance variable in the constructor that is assigned an order object
        self.order = Order ()



# For loop:

    # Adding 100 customers into queue:

    # Customer's name as key in dictionary:



# Print list of customers and total burgers ordered sorted by most number of burgers:

