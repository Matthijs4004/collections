from random import choice
import random

#Deel 1: Lists

colors = ["groen", "oranje", "blauw", "bruin"]

print("Hoeveel kleuren m&m's wil je aan de zak toevoegen?")
aantal = int(input("> "))


def listZak(aantal: int):
    colors_bag = []
    for i in range(aantal):
        color = choice(colors)
        colors_bag.append(color)
    else:
        return colors_bag


# Deel 2: Dictionary

mnmDict = {}

def dictZak(aantal:int): 
  for i in range(aantal): 
    mnmColor = random.randint(0,3) 
    if not colors[mnmColor] in mnmDict:
      mnmDict[colors[mnmColor]] = 1
    else:
      mnmDict[colors[mnmColor]] += 1
  return mnmDict 


# Deel 3: sorteren

def mnmSort(mnmList, colors):
    if isinstance(mnmList, list):
        nieuweZak = sorted(mnmList)
    else:
        nieuweZak = {}
        for color in mnmList:            
            nieuweZak[color] = mnmList[color]
    return nieuweZak

print(mnmSort(listZak(aantal), colors))
print(mnmSort(dictZak(aantal), colors))