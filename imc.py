poids = float(input("Entrez votre poids en kg\n"))
taille = float(input("Entrez votre taille en mètres\n"))

imc = poids / taille ** 2

if imc<18.5: 
    print("Insuffisance pondérale\nVotre IMC est de ",imc)
elif 18.5 <= imc <25:
    print("Corpulence normale\nVotre IMC est de ",imc)
elif 25 <= imc <30:
    print("Surpoids\nVotre IMC est de ",imc)
elif imc >= 30:
    print("Obesité\nVotre IMC est de ",imc)        
     