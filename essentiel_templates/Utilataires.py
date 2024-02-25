class Etudiant:
  def __init__(self,matricule, nom, prenom, genre, note):
    self.matricule = matricule
    self.nom = nom
    self.prenom = prenom
    self.genre = genre
    self.note = note

  def nom_complet(self):
    return f"{self.prenom} {self.nom}"

  def genre_entier(self):
    if self.genre == 'M':
      return "Masculin"
    else:
      return "Féminin"

  def moyenne(self):
    if self.note >= 16:
      return "Très bien"
    elif self.note >= 14:
      return "Bien"
    elif self.note >= 14:
      return "Assez Bien"
    elif self.note >= 10:
      return "Passable"
    else:
      return "Non Admis"