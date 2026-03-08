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
            self.voitureservice = voiture
            voiture.chauffeur = self
        else:
            print(f"L'employé possède déja une voiture")


    def retirervoiture(self):
        if self.voitureservice is None:
            print(" Cet employé ne possède pas de voiture de service")
        else:
            self.voitureservice = None