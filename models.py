class Carte:
  def __init__(self, id, recto, verso, isReversible):
      self.id = id
      self.recto = recto
      self.verso = verso
      self.isReversible = isReversible

class CarteUtil(Carte):
  def __init__(self, id, recto, verso, isReversible, date=0):
    Carte.__init__(self, id, recto, verso, isReversible)
    self.date = date

class Paquet:
  def __init__(self, id, listeCartes = []):
    self.id = id
    self.listeCartes = listeCartes
      


class Session:
  def __init__(self, cartes = [], configCompartiments = [1, 2, 8, 16, 32, 180, 360]):
    self.cartes = cartes
    self.configCompartiments = configCompartiments
    self.initCompartiments()

  def initCompartiments(self) :
    self.compartiments = [[] for _ in range(len(self.configCompartiments))]


  def getQuestion() :
    return

  def valideQuestion(question) :
    return

  def ajoute_carte(self, carte):
    self.compartiments[0].append(carte)

  def suprimer_carte(self, carte):
    for n in range (0, len(self.compartiments)-1):
      self.compartiments[n].remove(carte)

  def augmenter(self, carte):
    for n in range (len(self.compartiments)):
      if carte in self.compartiments[n]:
        if not ((n+1) > len(self.compartiments)-1):
          self.compartiments[n+1].append(carte)
          self.compartiments[n].remove(carte)
        break

  def baisser(self, carte):
    for n in range (len(self.compartiments)):
      if carte in self.compartiments[n]:
        if not (n == 0):
          self.compartiments[n-1].append(carte)
          self.compartiments[n].remove(carte)

def printSession(session: Session) :
  for i in range(len(session.compartiments)):
    print("Compartiment " + str(i))
    for carte in session.compartiments[i] :
      print("    "+carte.recto)

paquet = Paquet(1, [
  CarteUtil(1, "Question 1", "Réponse 1", True),
  CarteUtil(2, "Question 2", "Réponse 2", True),
  CarteUtil(3, "Question 3", "Réponse 3", True),
  CarteUtil(4, "Question 4", "Réponse 4", True),
  CarteUtil(5, "Question 5", "Réponse 5", True),
  CarteUtil(6, "Question 6", "Réponse 6", True),
  CarteUtil(7, "Question 7", "Réponse 7", True),
  CarteUtil(8, "Question 8", "Réponse 8", True),
  CarteUtil(9, "Question 9", "Réponse 9", True),
  CarteUtil(10, "Question 10", "Réponse 10", True)
])

carte1 = paquet.listeCartes[0]
masession = Session()

masession.ajoute_carte(carte1)
printSession(masession)
for n in range(0, len(masession.compartiments)):
  masession.augmenter(carte1)
  printSession(masession)
  print("stop"+str(n))
masession.baisser(carte1)
printSession(masession)
print(carte1.date)




