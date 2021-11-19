import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList):
    number = random.randrange(3,11)
    print(random.choices(spelList, k = number))

spelProgramma(spelList)