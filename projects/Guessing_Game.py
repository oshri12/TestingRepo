import random

choice = random. randint(1, 100)

print (choice)
g=int(input('Choose one of the options: 1.too high 2.too low 3.Bingo: '))
counter=1
min=0
max=100
while g!=3:
    if g==1:
        if choice<max:
            max=choice

    elif  g==2:
        if choice > min:
            min = choice
    choice = random.randint(min+1, max-1)
    counter += 1
    print(choice)
    g = int(input('Choose one of the options: 1.too high 2.too low 3.Bingo: '))


print(f'your number is {choice} and the number of guesses is {counter}' )