"""This code will ask the user for what pizzas they want and how many they need and if 0 will exclude the pizza from final answer"""
#variables for storage
listpizza = []
stop = 0



#loop until right option for cheese
while True:
    try:

        cheese = int(input("How many cheese pizzas do we want? "))
        if cheese > stop:
            listpizza.append(cheese)
            break
        if cheese == stop:
            listpizza.append(cheese)
            break
        if cheese < stop:
            print("Please enter a valid amount")
    except ValueError:
        print("Please enter a valid amount")
while True:#loop until right option for chicken
    try:

        chicken = int(input("How many chicken pizzas do we want? "))
        if chicken > stop:
            listpizza.append(chicken)
            break
        if chicken == stop:
            listpizza.append(cheese)
            break
        if chicken < stop:
            print("Please enter a valid amount")
    except ValueError:
        print("Please enter a valid amount")
while True:#loop until right option for pepperoni
    try:

        pepperoni = int(input("How many pepperoni pizzas do we want? "))
        if pepperoni > stop:
            listpizza.append(pepperoni)
            break
        if pepperoni == stop:
            listpizza.append(cheese)
            break
        if pepperoni < stop:
            print("Please enter a valid amount")
    except ValueError:
        print("Please enter a valid amount")
while True:#loop until right option for veggie
    try:

        veggie = int(input("How many veggie pizzas do we want? "))
        if veggie > stop:
            listpizza.append(veggie)
            break
        if veggie == stop:
            listpizza.append(cheese)
            break
        if veggie < stop:
            print("Please enter a valid amount")
    except ValueError:
        print("Please enter a valid amount")

#print the wanted order

if listpizza[0] != stop: #!= stop makes it so it wont print if the value of the variable is 0 
    print(f"Cheese: {listpizza[0]}")
if listpizza[1] != stop:
    print(f"Chicken: {listpizza[1]}")
if listpizza[2] != stop:
    print(f"Pepperoni: {listpizza[2]}")
if listpizza[3] != stop:
    print(f"Veggie: {listpizza[3]}")
        
        


