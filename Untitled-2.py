stop = 0
min = 1.2 # min value
volt_list = []
while True:
    try:
        volt = float(input('Enter your input: '))
        while volt >= stop:
            volt_list.append(volt)  # adding item to list
            volt = float(input('Enter your input: '))
        break
    except ValueError:
        print('Not robot compliant!')
for item in volt_list:
    if item >= min: # comparing 
        print('Beep')
    else:
        print('Boop')