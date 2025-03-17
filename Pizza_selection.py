"""This code will ask the user for what pizzas they want and how many they need and if 0 will exclude the pizza from final answer"""
#variables for storage
listpiz = []


chicken = input("How many chicken pizzas do we want? ")
pepper = input("How many pepperoni pizzas do we want? ")
veggie = input("How many veggie pizzas do we want? ")
#loop until right option for cheese
while True:
    try:

        cheese = input("How many cheese pizzas do we want? ")
        cheese = int()
        
