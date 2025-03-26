"""this code will ask the user for a speed, then display to them the unsafe speeds they have inputting."""
#define variables for the code

good_descent = 10 
bad_speed = 0
stop = 'terminate' #stop requirement
zero = 0 
 

#define lists of all speeds 
speedlist = []

#ask the user to input
speed = input('Input descent speed in m/s: ')
#loop to keep on asking for input until code is terminated
while speed != stop:# making the code run until 'terminate' is entered 
    #check for valid speed 
    try:
        speedlist.append(float(speed))#append to list 
    except: #check for valid input 
        print('Error, invalid input.')
    speed = input('Input descent speed in m/s: ')


#find the amount of shuttles too fast. 
for item in speedlist:
    if item > good_descent:
        bad_speed += 1 




#print the number of too fast shuttles
if bad_speed != 1:
    print(f"There were {bad_speed} space shuttles faster than the safe speed.")
else:
    print(f"There was 1 space shuttle faster than the safe speed.")

if bad_speed > 1: #check if there isnt 0 fast shuttles, so that we know there is something to print
    print("The unsafe speeds are")
    for item in speedlist:
        if float(item) > good_descent:
            print(item)
elif bad_speed == 1:
    print("The unsafe speed was")
    for item in speedlist:
        if float(item) > good_descent:
            print(item)
            
else:  #passes because there are zero too fast space shuttles
    pass
    


