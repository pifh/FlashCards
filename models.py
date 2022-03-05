class Carte:
  def __init__(self, recto, verso):
      self.recto = recto
      self.verso = verso


class Session:
  def __init__(self, cartes = [], configCompartiments = [1, 2, 8, 16, 32, 180, 360]):
    self.cartes = cartes
    self.configCompartiments = configCompartiments
    self.compartiments = [[] for _ in range(7)]

  def initCompartiements(self, configCompartiments = [1, 2, 8, 16, 32, 180, 360]) :
    self.configCompartiments = configCompartiments
    self.compartiments = [[] for _ in range(self.configCompartiments)]


  def getQuestion() :
    return

  def valideQuestion(question) :
    return

