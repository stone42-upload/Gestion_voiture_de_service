from voitures_affectées import voiture_poss

class Employe:
    en_affichage = False

    def __init__(self, numeropermis, nom, prenom, voitureservice=None):
        self.numeropermis = numeropermis
        self.nom = nom
        self.prenom = prenom
        self.voitureservice = voitureservice

    def afficherinformation(self):
        Employe.en_affichage = True
        print(f"Employé : {self.nom} {self.prenom}")
        print(f"Numéro de permis : {self.numeropermis}")
        print("---------------------------------------------")

        if self.voitureservice is None:
            print("Cet employé n'a aucune Voiture de service")
            print("")

        else:
            print("Voiture de service :")
            self.voitureservice.afficherinformation()
            print("")

        Employe.en_affichage = False

    def affectervoiture(self, voiture):
        if self.voitureservice is None:
            if voiture_poss.count(voiture) < 1:
                voiture_poss.append(voiture)
                self.voitureservice = voiture
                voiture.chauffeur = self
            else:
                print(f"Cette voiture a déja été attribuer à {voiture.chauffeur.nom} {voiture.chauffeur.prenom}")

        else:
            print(f"L'employé possède déja une voiture")


    def retirervoiture(self):
        if self.voitureservice is None:
            print(" Cet employé ne possède pas de voiture de service")
        else:
            voiture = self.voitureservice
            voiture_poss.remove(voiture)
            voiture.chauffeur = None
            self.voitureservice = None