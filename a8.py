# Camden Hatch, Rasa Ichimori, Machael Backman, Porter Rasmussen
# Section 4
# This program tracks exactly how many hamburgers each customer eats.  

# Import random for generating random numbers
import random

# Order Class 
class Order (): 
    # Constructor
    def __init__(self):
    # Instance variable to store the number of burgers in the order
        self.burger_count = self.randomBurgers()

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
    def randomName(self) :
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen",
                       "Invisible Swordsman", "Singing Bush"]
        # Randomly returns one of the 9 names when called
        index = random.randint(0, len(lstCustomers) - 1)
        return lstCustomers[index]


# Customer Class 
class Customer (Person): 
    # Constructor class that inherits from parent Person class
    def __init__(self):
        super().__init__()
    # Instance variable in the constructor that is assigned an order object
        self.order = Order ()

# Variable for queue to assign customer items:
queueCustomer = []

# Variable for a dictionary with key as customer name (str) and values as total burgers ordered (int):
dictCustAndBurgCount = {}

# For loop:
for iCount in range (0, 99) :
    # Adding 100 customers into queue:
    # starts with creating a customer object:
    objCustomer = Customer ()
    # Append it to queue list: 
    queueCustomer.append(objCustomer)

    # Check if object name is already in dictionary:
    if objCustomer.customer_name in dictCustAndBurgCount :
        # Add order count to object in dictionary with same name:
        dictCustAndBurgCount[objCustomer.customer_name] += objCustomer.order.burger_count
    else :
        # Add customer's name as new key in dictionary and then give the loop the signal to continue to a new object:
        dictCustAndBurgCount[objCustomer.customer_name] = objCustomer.order.burger_count

    iCount += 1

    
# Print list of customers and total burgers ordered sorted by most number of burgers:
# Sort dictionary into a list based on value greatest to smallest:
lstCustSorted = sorted(dictCustAndBurgCount.items(), key=lambda x: x[1], reverse=True)

# Print this new list sorted from values in dictionary:
for iCount in range (0, (len(lstCustSorted) -1) ) :
    print(f"{lstCustSorted[iCount][0].ljust(19)} {lstCustSorted[iCount][1]}")
    
    iCount += 1