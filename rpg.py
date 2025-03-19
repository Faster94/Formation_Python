import random

class Objet:
    def __init__(self, nom, effet):
        self.nom = nom
        self.effet = effet

    def utiliser(self, cible):
        if self.effet == "soin":
            cible.points_de_vie += 30
            print(f"{cible.nom} récupère 30 PV!")
        elif self.effet == "force":
            cible.attaque += 5
            print(f"{cible.nom} voit son attaque augmenter de 5!")

class Hero:
    def __init__(self, nom):
        self.nom = nom
        self.points_de_vie = 100
        self.attaque = 10
        self.niveau = 1
        self.experience = 0
        self.inventaire = {}
        self.competences = {}
        self.effets = {}

    def attaquer(self, monstre):
        print(f"{self.nom} attaque {monstre.nom} et inflige {self.attaque} dégâts!")
        monstre.points_de_vie -= self.attaque
        if monstre.points_de_vie <= 0:
            print(f"{monstre.nom} est vaincu!")
            self.gagner_experience(20)

    def gagner_experience(self, points):
        self.experience += points
        if self.experience >= 50 * self.niveau:
            self.niveau += 1
            self.attaque += 5
            self.points_de_vie += 20
            self.experience = 0
            print(f"{self.nom} monte au niveau {self.niveau}! Attaque et vie augmentées!")

    def ajouter_objet(self, objet, quantite):
        if objet.nom in self.inventaire:
            self.inventaire[objet.nom] += quantite
        else:
            self.inventaire[objet.nom] = quantite
        print(f"{objet.nom} ajouté à l'inventaire ({self.inventaire[objet.nom]} en stock).")

    def utiliser_objet(self, objet):
        if objet.nom in self.inventaire and self.inventaire[objet.nom] > 0:
            self.inventaire[objet.nom] -= 1
            print(f"{self.nom} utilise {objet.nom}!")
            objet.utiliser(self)
        else:
            print(f"{objet.nom} n'est pas disponible.")

    def apprendre_competence(self, nom, degats):
        self.competences[nom] = degats
        print(f"{self.nom} apprend la compétence {nom}!")

    def utiliser_competence(self, nom, cible):
        if nom in self.competences:
            print(f"{self.nom} utilise {nom} et inflige {self.competences[nom]} dégâts à {cible.nom}!")
            cible.points_de_vie -= self.competences[nom]
        else:
            print(f"{self.nom} ne connaît pas cette compétence.")

    def appliquer_effet(self, nom, duree):
        self.effets[nom] = duree
        print(f"{self.nom} est affecté par {nom} pendant {duree} tours!")

    def mettre_a_jour_effets(self):
        for effet in list(self.effets.keys()):
            self.effets[effet] -= 1
            if self.effets[effet] <= 0:
                print(f"L'effet {effet} sur {self.nom} se dissipe.")
                del self.effets[effet]

class Monstre:
    def __init__(self, nom, points_de_vie, attaque):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque

    def attaquer(self, hero):
        print(f"{self.nom} attaque {hero.nom} et inflige {self.attaque} dégâts!")
        hero.points_de_vie -= self.attaque
        if random.random() < 0.2:  # 20% de chance d'empoisonner
            hero.appliquer_effet("poison", 3)

# Combat de démonstration
hero = Hero("Arthur")
monstre = Monstre("Gobelin", 50, 8)
hero.apprendre_competence("Coup Puissant", 15)
potion = Objet("potion", "soin")
hero.ajouter_objet(potion, 2)

while hero.points_de_vie > 0 and monstre.points_de_vie > 0:
    hero.attaquer(monstre)
    if monstre.points_de_vie > 0:
        monstre.attaquer(hero)
        hero.mettre_a_jour_effets()
    print(f"PV {hero.nom}: {hero.points_de_vie} PV {monstre.nom}: {monstre.points_de_vie}\n")
    
if hero.points_de_vie > 0:
    print(f"{hero.nom} a gagné le combat!")
else:
    print(f"{monstre.nom} a vaincu {hero.nom}...")