class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage, chauffeur=None):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = chauffeur

    def afficherinformation(self):
        print(f"matricule: {self.matricule}, annee: {self.annee}, marque: {self.marque}, kilometrage: {self.kilometrage}")

        if(self.chauffeur is None):
            print("Cette voiture n'a pas encore été attribuer")
            print("")

        else:
            print("chauffeur")
            self.chauffeur.afficherinformation()
            print("")
