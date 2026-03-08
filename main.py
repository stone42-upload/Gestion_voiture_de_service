from Employe import Employe
from Voiture import Voiture

Employe1 = Employe("A1234-56783-12845", "Georges", "Winteral")
Employe2 = Employe("B5837-97832-67249", "Harry", "Potter")
Employe3 = Employe("F5482-75954-78135", "Luis", "Nova")

Voiture1 = Voiture("ABCJ 123", 2020,"volswagen", 45000)
Voiture2= Voiture("123 ABC", 2018, "Honda", 78000)
Voiture3 = Voiture("KLM-9087", 2023, "Ford", 15000)



Employe1.afficherinformation()
Employe2.afficherinformation()
Employe3.afficherinformation()

Voiture1.afficherinformation()
Voiture2.afficherinformation()
Voiture3.afficherinformation()

Employe1.affectervoiture(Voiture1)
Employe1.afficherinformation()

Employe2.affectervoiture(Voiture2)
Employe2.afficherinformation()

Employe1.retirervoiture()
Employe1.afficherinformation()

Employe3.affectervoiture(Voiture2)

