class Employe:
    def __init__(self, numeropermis, nom, prenom, voitureservice=None):
        self.numeropermis = numeropermis
        self.nom = nom
        self.prenom = prenom
        self.voitureservice = voitureservice

    def afficherinformation(self):
        print(f"Employé : {self.nom} {self.prenom}")
        print(f"Numéro de permis : {self.numeropermis}")

        if self.voitureservice is None:
            print("Cet employé n'a aucune Voiture de service")
            print("")

        else:
            print("Voiture de service :")
            self.voitureservice.afficherinformation()
            print("")

    def affectervoiture(self, voiture):
        if self.voitureservice is None:
            self.voitureservice = voiture
        else:
            print(f"L'employé possède déja une voiture")

    def retirervoiture(self):
        if self.voitureservice is None:
            print(" Cet employé ne possède pas de voiture de service")
        else:
            self.voitureservice = None