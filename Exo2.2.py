score = int(input("Quel est le score de l'élève?\n"))

if 0 <= score <= 39: 
    print("Vous avez une note de F ")
elif 40 <= score <= 49:
    print("Vous avez une note de E")
elif 50 <= score <= 59:
    print("Vous avez une note de D")
elif 60 <= score <= 69:
    print("Vous avez une note de C")
elif 70 <= score <= 79:
    print("Vous avez une note de B")
elif 80 <= score <= 89:
    print("Vous avez une note de A")
elif 90 <= score <= 100:
    print("Vous avez une note de S")
else :
    print("Score entré incorrect")


