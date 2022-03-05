class Carte:
  def __init__(self, id, recto, verso, isReversible):
      self.id = id
      self.recto = recto
      self.verso = verso
      self.isReversible = isReversible

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