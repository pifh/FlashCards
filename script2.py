from gettext import lngettext
from random import *
from question import *


questions = [
  Question("Question 1", "Réponse 1"),
  Question("Question 2", "Réponse 2"),
  Question("Question 3", "Réponse 3"),
  Question("Question 4", "Réponse 4"),
  Question("Question 5", "Réponse 5"),
  Question("Question 6", "Réponse 6"),
  Question("Question 7", "Réponse 7")
]

questions_valides = []

n = 1
question = questions[n]

print(question.question)
input()
print(question.reponse)
validation = input("+ ou - ?")
questions_valides.append(question)
questions.remove(question)
print(questions)
print(questions_valides)