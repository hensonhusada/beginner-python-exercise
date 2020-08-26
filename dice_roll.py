import random

stats = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

try:
    choice = int(input('How many times do you wanna roll the dice?'))
    if choice < 1:
        print('Quiting program')
        exit()
except ValueError:
    print('Quiting program')
    exit()

for i in range(choice):
    temp = random.randint(1,6)
    for key in stats:
        if temp == int(key):
            stats[key] += 1

print('\n')
print('This is how much each die you get:')
for key in stats:
    print(key, ':', stats[key])