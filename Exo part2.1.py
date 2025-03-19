

my_age = 25
#print(my_age, type(my_age))

your_age = int(input("Entrez votre âge\n"))
#print(your_age, type(your_age))

diff = abs(my_age - your_age)
#print(diff, type(diff))

if diff > 1 :
    print("Vous avez" ,diff, "ans de plus que moi")
elif diff == 1 :
    print("Vous avez" ,diff,"an de plus que moi")
elif diff == 0 :
    print("On a le même âge !")