import random

def test_number(number, answer):
    global score
    if number > answer:
        print('Too high')
        score -= 1
    elif number < answer:
        print('Too low')
        score -= 1
    else:
        print('You guessed right!')
        return True

def check_input():
    while True:
        try:
            choice = int(input("Guess Number: "))
            if choice <1 or choice>100:
                print('Guess out of bound!')
            else:
                return choice
        except ValueError:
            print('Wrong Input!')
        
score = 100
print('Guess between 1-100! Max score = 100')
answer = random.randint(1,100)
guess = False

while not guess:
    choice = check_input()
    guess = test_number(choice, answer)
print('Your score: %s' % score)