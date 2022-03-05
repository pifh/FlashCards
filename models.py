from random import *

class Carte:
  def __init__(self, id, recto, verso, isReversible):
      self.id = id
      self.recto = recto
      self.verso = verso
      self.isReversible = isReversible

class CarteUtil(Carte):
  def __init__(self, id, recto, verso, isReversible, vue=False):
    Carte.__init__(self, id, recto, verso, isReversible)
    self.vue = vue

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

  def ajoute_paquet(self, paquet):
    for n in range(len(paquet.listeCartes)):
      self.ajoute_carte(paquet.listeCartes[n])


  def suprimer_carte(self, carte):
    for n in range (0, len(self.compartiments)-1):
      self.compartiments[n].remove(carte)

  def augmenter(self, carte):
    carte.vue = True
    for n in range (len(self.compartiments)):
      if carte in self.compartiments[n]:
        if not ((n+1) > len(self.compartiments)-1):
          self.compartiments[n+1].append(carte)
          self.compartiments[n].remove(carte)
        break

  def baisser(self, carte):
    carte.vue = True
    for n in range (len(self.compartiments)):
      if carte in self.compartiments[n]:
        if not (n == 0):
          self.compartiments[n-1].append(carte)
          self.compartiments[n].remove(carte)

  def getJour(self):
    return 1
  
  def initVue(self):
    for compartiment in self.compartiments:
      for carte in compartiment:
        carte.vue = False 
  
  def nonVue(self, compartiments):
    LnonVue = []
    for carte in compartiments:
      if not carte.vue  :
        LnonVue.append(carte)
    return LnonVue


def printSession(session: Session) :
  for i in range(len(session.compartiments)):
    print("Compartiment " + str(i))
    for carte in session.compartiments[i] :
      print("    "+carte.recto)

paquet1 = Paquet(1, [
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


masession = Session()

def tire_une_carte():
  for n in range(len(masession.compartiments)):
    print("compartiment "+ (str(n+1)))
    lnonvue = masession.nonVue(masession.compartiments[n]) 
    if len(lnonvue) == 0:
      print("rien") 
    while (len(lnonvue) > 0) :
      i = randint(0, len(lnonvue)-1)
      print(lnonvue[i].recto)
      input()
      print(lnonvue[i].verso)
      validation = input("+ ou - ?")
      if (validation == "+"):
        masession.augmenter(lnonvue[i])
      else:
        masession.baisser(lnonvue[i])
      lnonvue = masession.nonVue(masession.compartiments[n])

masession.ajoute_paquet(paquet1)
tire_une_carte()


