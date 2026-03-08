import Employe


class Voiture:
    en_affichage = False

    def __init__(self, matricule, annee, marque, kilometrage, chauffeur=None):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = chauffeur

    def afficherinformation(self):
        print(f"  matricule: {self.matricule}")
        print(f"  annee: {self.annee}")
        print(f"  marque: {self.marque}")
        print(f"  kilometrage: {self.kilometrage}")

        if Employe.Employe.en_affichage:

            if self.chauffeur is None:
                print("Cette voiture n'a pas encore été attribuer")
                print("")

            else:
                pass

        else:
            if self.chauffeur is None:
                print("  Cette voiture n'a pas encore été attribuer")

            else:
                print("Chauffeur: ")
                self.chauffeur.afficherinformation()
        print("")



