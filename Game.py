from random import randint
meine_zahl = randint(1, 10)
deine_zahl = int(input("Zahl?"))
while True:
    if deine_zahl > meine_zahl:
        print("Deine Zahl ist grösser")
    if deine_zahl < meine_zahl:
        print("Deine Zahl ist kleiner")
    if deine_zahl == meine_zahl:
        print("Bingo")
break
