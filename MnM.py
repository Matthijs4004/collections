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

def dictZak(aantal:int): #function met parameter -> int
  for i in range(aantal): 
    mnmColor = random.randint(0,3) #random number generator tussen 0-3
    if not mnmList[mnmColor] in mnmDict: #mnmcolor geeft een nummber tussen 0-3 en die wordt gecheckt door de list, als die niet in de dict zit wordt die toegevoegd zo niet dat wordt er wat bij gedaan
      mnmDict[mnmList[mnmColor]] = 1
    else:
      mnmDict[mnmList[mnmColor]] += 1
  return mnmDict #return de mnmdict zodat hij de juiste output geeft en niet 'none'

print(dictZak(aantal))

# Deel 3: sorteren

def mnmSort(sorteer):
    print(sorteer)



mnmSort(dictZak(aantal))