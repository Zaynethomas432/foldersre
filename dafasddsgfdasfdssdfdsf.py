
min = 80 # min value
done = 'done'
smartstudent = 0
smartlist = []
brain = input("Enter a score, or type 'done' to exit: ")
while brain != done: #loop
    try:
        smartlist.append(int(brain))#add to list
    except: #make sure valid
        print('Invalid score!')
    brain = input("Enter a score, or type 'done' to exit: ")

for item in smartlist:
    if item >=   min:
        smartstudent += 1

if smartstudent != 1:
    print(f'This class has {smartstudent} smart students!')
else:
    print(f'This class has 1 smart student!')