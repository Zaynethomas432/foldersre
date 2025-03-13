stop = 0
min = 34 # min value
max = 42
heat = []
while True:
    try:
        temps = input('Enter the temperature: ')
        temp = int(temps)
        while temp != -1:
            heat.append(temp)  # adding item to list
            temps = input('Enter the temperature: ')
            temp = int(temps)
        break
    except ValueError:
        print('Invalid temperature.')
    if temps == -1:
        break
for item in heat:
    if item > max: # comparing 
        print('too hot')
    elif item < min:
        print('too cold')
    else:
        print('just right')