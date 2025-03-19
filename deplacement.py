print("Stack A")
liste = [1,0,0,0,0,0,0]
position = 0
print(liste)

while (1):
    deplacement = int(input("Entrez le déplacement : "))
    liste[position] = 0
    liste[position + deplacement] = 1
    print(liste)
    position = position + deplacement 
    if (deplacement == 0):
        break
