import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList, minimum, maximum):
    number = random.randrange(minimum,maximum)
    print(random.choices(spelList, k = number))

spelProgramma(spelList,3,11)