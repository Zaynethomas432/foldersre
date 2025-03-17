"""This code will ask the user for what pizzas they want and how many they need and if 0 will exclude the pizza from final answer"""
#variables for storage
listpiz = []
stop = 0



#loop until right option for cheese
while True:
    try:

        cheese = int(input("How many cheese pizzas do we want? "))
        if cheese > stop:
            listpiz.append(cheese)
            break
        if cheese == stop:
            break
    except ValueError:
        print("Please enter a valid amount")
while True:
    try:

        chicken = int(input("How many chicken pizzas do we want? "))
        if chicken > stop:
            listpiz.append(chicken)
            break
        if chicken == stop:
            break
    except ValueError:
        print("Please enter a valid amount")
while True:
    try:

        pepperoni = int(input("How many pepperoni pizzas do we want? "))
        if pepperoni > stop:
            listpiz.append(pepperoni)
            break
        if pepperoni == stop:
            break
    except ValueError:
        print("Please enter a valid amount")
while True:
    try:

        veggie = int(input("How many veggie pizzas do we want? "))
        if veggie > stop:
            listpiz.append(veggie)
            break
        if veggie == stop:
            break
    except ValueError:
        print("Please enter a valid amount")
    #print the wanted order
for i in range(0,1):
    if cheese != stop:
        print(f"Cheese: {listpiz[0]}")
    if cheese != stop:
        print(f"Chicken: {listpiz[1]}")
    if cheese != stop:
        print(f"Pepperoni: {listpiz[2]}")
    if cheese != stop:
        print(f"Veggie: {listpiz[3]}")
        
        


