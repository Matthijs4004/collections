import random

mnmlist = ["groen", "oranje", "blauw", "bruin"]

print("Hoeveel kleuren m&m's wil je aan de zak toevoegen?")
aantal = int(input("> "))

def listZak(x):
  print(random.choices(mnmlist, k=x))

listZak(aantal)

