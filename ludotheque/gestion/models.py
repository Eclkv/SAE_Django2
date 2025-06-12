from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Editeur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Jeu(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    annee_sortie = models.PositiveIntegerField(null=True, blank=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.SET_NULL, null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    editeur = models.ForeignKey(Editeur, on_delete=models.SET_NULL, null=True, blank=True)
    photo_boite = models.ImageField(upload_to='boites/', null=True, blank=True)

    def __str__(self):
        return self.titre


class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Commentaire(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    texte = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.joueur} sur {self.jeu}"
