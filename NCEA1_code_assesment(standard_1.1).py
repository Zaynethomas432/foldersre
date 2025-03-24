"""this code will ask the user for a speed, then display to them the unsafe speeds they have inputting."""
#define variables for the code
stop = 'terminate'
good_descent = 10
bad_speed = 0
#define lists of all speeds 
speedlist = []
#ask the user to input
speed = input('Input descent speed in m/s: ')
#loop to keep on asking for input until code is terminated
while speed != stop:# making the code run until 'terminate' is entered 
    #check for valid speed
    try:
        speedlist.append(float(speed))#append to list
    except:
        print('Error, invalid input.')
    speed = input('Input descent speed in m/s: ')


    


