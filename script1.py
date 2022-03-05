from models import Carte, Paquet, Session

paquet = Paquet(1, [
  Carte(1, "Question 1", "Réponse 1", True),
  Carte(2, "Question 2", "Réponse 2", True),
  Carte(3, "Question 3", "Réponse 3", True),
  Carte(4, "Question 4", "Réponse 4", True),
  Carte(5, "Question 5", "Réponse 5", True),
  Carte(6, "Question 6", "Réponse 6", True),
  Carte(7, "Question 7", "Réponse 7", True),
  Carte(8, "Question 8", "Réponse 8", True),
  Carte(9, "Question 9", "Réponse 9", True),
  Carte(10, "Question 10", "Réponse 10", True)
])



session = Session()
for carte in paquet.listeCartes :
  session.ajoute_carte(carte)

print(session.compartiments[0])

def printSession(session: Session) :
  for i in range(len(session.compartiments)):
    print("Compartiment " + str(i))
    for carte in session.compartiments[i] :
      print("    "+carte.recto)

printSession(session)