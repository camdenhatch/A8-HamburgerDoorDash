A8 – Hamburger Door Dash (Group)
THIS IS A GROUP ASSIGNMENT
Your task is to create a program that will help you familiarize yourself with various data structures available in the Python language. 
You are the owner of a very successful hamburger restaurant. Your faithful customers line up every day and eat dozens of burgers. You are writing a program to track exactly how many hamburgers each customer eats. 
•	Create an Order class
o	Create a constructor that defines an instance variable called burger_count
o	Create a method called randomBurgers that returns a number between 1 and 20
o	The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable
•	Create a Person class
o	Create a constructor that defines an instance variable called customer_name
o	Create a method called randomName() that contains a list of 9 names:
        lsCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
o	This method randomly returns one of the 9 names when called
o	The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name instance variable
•	Create a Customer class that inherits from the Person class
o	Create a constructor that calls the parent constructor
o	Create an instance variable called order in the constructor that is assigned an order object
•	Create a variable for a Queue that will be assigned items of type Customer 
o	This variable will represent your line of customers (objects) waiting outside to place their hamburger orders
•	Create a variable for a Dictionary with keys of type string and values of type int.
o	The key will be the customer name. The value will be the total number of burgers that that customer has ever ordered.
•	Put 100 customers into the queue (a for loop is good for this). Each customer object will already have a random number of burgers for each order when you create the customer object, so you just need to append the customer to the queue list.
•	In the for loop, also put the customer’s name in the dictionary as a key, and the number of burgers they ordered as the value.
o	But remember that dictionary keys are unique! So check if that customer name is already in the dictionary before adding it in. If the customer name is already in the dictionary, then add the number of burgers in that order to the total number of burgers (the value for the customer in the dictionary). Otherwise, add the customer name to the dictionary with the initial number of burgers in the order to the dictionary.
•	Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
NOTE: Remember that a queue in Python is a list data structure. Also, the randint() method from the random class returns a random number. For example:
iRandomNum = random.randint(0,8)
This returns a random integer between 0 and 8 (9 numbers).
iRandomBurger = random.randint(1, 20)
This would return a random number between 1 and 20.
Sample Output 

Your sample output could look like:

 
You can use a statement similar to: listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True) 
NOTE: The listSortedCustomers is a new list variable, not a dictionary. Dictionaries cannot be sorted so this statement sorts the data from the dictionary and stores it to a list. For each item in the list (representing a customer) there will be two positions 0 and 1. Position 0 contains the previous dictionaries key and position 1 contains the value. 
Now display the customer name and the total number of burgers consumed. Do this using a for loop displaying the contents of the list in positions 0 and 1. 
Make the customer name an even sized value using the ljust() function with the value of 
19 as the parameter like customer[0].ljust(19) where customer is each list item object in the for loop.