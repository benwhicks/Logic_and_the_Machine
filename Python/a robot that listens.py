whoilike = "David"
colorilike = "Blue"

you = input("What is your name? ")
if you == whoilike:
    print("I like people called " + whoilike + "!")
else:
    print("I guess you could call yourself " + you + " if you had to. ")


favcolor = input("What is your favourite colour? ")
if favcolor == colorilike:
    print("I like " + colorilike + " too! ")
else:
    print("Ewww.")

if (you == whoilike and favcolor == colorilike):
    print("Let’s be friends!")
