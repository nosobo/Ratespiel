# Python Game where the player guesses a randomly generated number between 0 and 100
from numpy import random

# Introduction to the the game
print("Hallo und herzlich willkommen! Ich lade dich ein, ein kleines Zahlenratespiel mit mir zu spielen!\n"
      "Ich habe eine natürliche Zahl zwischen 0 und 100 erstellt und du sollst sie erraten.")
# This function generates a pseudorandom integer number between 0 and 100
# Number is assigned to variable "gesuchtezahl"
gesuchtezahl = random.randint(0, 100)
# print(gesuchtezahl)

# This function takes keyboard input from the player
# Keyboard input is assigned to the variable "eingabezahl"
eingabezahl = input("Gib eine Zahl zwischen 0 und 100 ein!\n")

# Cast operator to convert the keyboard input of type String to a float value
eingabezahl = float(eingabezahl)
# Cast operator to convert the input of type String to an int value
# zahl2 = int(zahl2)

# Program runs as long as eingabezahl doesn't meet gesuchtezahl
while gesuchtezahl != eingabezahl:
    if eingabezahl < gesuchtezahl:
        print("Leider falsch! Die eingegebene Zahl ist kleiner als die gesuchte Zahl. Bitte versuche es erneut.")
        eingabezahl = input("Gib eine Zahl zwischen 0 und 100 ein!\n")
        eingabezahl = float(eingabezahl)
    elif eingabezahl > gesuchtezahl:
        print("Leider falsch! Die eingegebene Zahl ist größer als die gesuchte Zahl. Bitte versuche es erneut.")
        eingabezahl = input("Gib eine Zahl zwischen 0 und 100 ein!\n")
        eingabezahl = float(eingabezahl)
else:
    print("Hezlichen Glückwunsch, du hast die gesuchte Zahl gefunden!")
