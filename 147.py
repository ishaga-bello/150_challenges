import random

color = ['red', 'blue', 'red', 'green']

myColor = ['gren', 'red', 'red', 'blue']

for i in range(0, 4):
    for j in range(0, 4):
        if color[i] == myColor[j]:
            print(color[i])