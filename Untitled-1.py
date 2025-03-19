print("Stack A")
tableau = [[1,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
posX = 0
posY = 0
for line in tableau:
    print(line)

while (1):
    deplacementX = int(input("Entrez le déplacement X : "))
    deplacementY = int(input("Entrez le déplacement Y : "))

    tableau[posY][posX] = 0
    tableau[posY + deplacementY][posX + deplacementX] = 1

    posX = posX + deplacementX
    posY = posY + deplacementY

    for line in tableau:
        print(line)

    if (deplacementX == 0 and deplacementY == 0):
        break