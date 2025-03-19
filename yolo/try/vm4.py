import os

dicError = {0 : "Executé avec succès.", 2 : "Ligne de commande non valide.", 3 : "Un input n'est pas correct."}

def showAllVM():
    return os.system("az vm list --output table")

def createVM():
    name = input("Donne le nom de la VM : ")
    image = input("Donne le nom de l'image ! (Ubuntu ou Windows) : ")
    taille = input("Donne également la taille : (Standard_B1ls) : ")
    group = input("Donne moi le groupe : ")
    if image == "Ubuntu":
        os.system(f"az vm create -n {name} -g {group} --size {taille} --image Ubuntu2404 --generate-ssh-keys --custom-data @nginx.sh")
    elif image == "Windows":
        os.system(f"az vm create -n {name} -g {group} --size {taille} --image Win2022Datacenter --generate-ssh-keys")
    print("VM créé avec succès !")

def modifyVM():
    showAllVM()
    vm = input("Modifier quelle VM ? : ")
    group = input("Donnez le groupe : ")
    command = input("Stopper ou redémarrer la vm ? (stop/restart) : ")
    return os.system(f"az vm {command} -g {group} -n {vm}")

def deleteVM():
    print("----------------")
    showAllVM()
    name = input("Donnez la VM à supprimer : ")
    group = input("Donnez également son groupe : ")
    conf = input("Êtes vous sûr de supprimer la VM ? (y/n)")
    if conf == "y":
        os.system(f"az vm delete -n {name} -g {group} --yes")
        print(f"Suppresison de {name} effectué avec succès.")
    else:
        print(f"Suppresison de {name} annulé.")
        return

# 0 = Nickel / 2 = Mauvaise commande / 3 = Mauvais input
def errorCheck(r):
    if r:   # If return != 0
        print(f"Erreur numéro {r}, {dicError[r]}")

def main():
    print("Bienvenue sur AZ Manager. Choissisez ce que vous voulez faire:")
    while True:
        print("1. Afficher toutes les VM.")
        print("2. Créer une VM.")
        print("3. Supprimer une VM")
        print("4. Modifier une VM")
        choix = int(input())
        if choix == 1:
            errorCheck(showAllVM())
        elif choix == 2:
            errorCheck(createVM())
        elif choix == 3:
            errorCheck(deleteVM())
        elif choix ==4:
            errorCheck(modifyVM())
        else:
            print("Wrong input")

main()
