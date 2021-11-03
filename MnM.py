import random

#Deel 1: Lists

mnmList = ["groen", "oranje", "blauw", "bruin"]

print("Hoeveel kleuren m&m's wil je aan de zak toevoegen?")
aantal = int(input("> "))

def listZak(x):
  print(random.choices(mnmList, k=x))

listZak(aantal)

# Deel 2: Dictionary

mnmDict = {}

def dictZak(aantal:int):
  for i in range(aantal):
    mnmColor = random.randint(0,3)
    if not mnmList[mnmColor] in mnmDict:
      mnmDict[mnmList[mnmColor]] = 1
    else:
      mnmDict[mnmList[mnmColor]] += 1
  return mnmDict


print(dictZak(aantal))