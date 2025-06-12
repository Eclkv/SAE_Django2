from django.urls import path
from .views import *
from django.shortcuts import render

# Vue d'accueil qui affiche un template
def accueil(request):
    return render(request, 'gestion/accueil.html')

urlpatterns = [
    # Accueil
    path('', accueil, name='accueil'),

    # Jeux
    path('jeux/', ListeJeux.as_view(), name='liste_jeux'),
    path('jeux/ajouter/', AjouterJeu.as_view(), name='ajouter_jeu'),
    path('jeux/modifier/<int:pk>/', ModifierJeu.as_view(), name='modifier_jeu'),
    path('jeux/supprimer/<int:pk>/', SupprimerJeu.as_view(), name='supprimer_jeu'),
    path('jeux/<int:pk>/', FicheJeu.as_view(), name='fiche_jeu'),

    # Auteurs
    path('auteurs/', ListeAuteurs.as_view(), name='liste_auteurs'),
    path('auteurs/ajouter/', AjouterAuteur.as_view(), name='ajouter_auteur'),
    path('auteurs/modifier/<int:pk>/', ModifierAuteur.as_view(), name='modifier_auteur'),
    path('auteurs/supprimer/<int:pk>/', SupprimerAuteur.as_view(), name='supprimer_auteur'),

    # Catégories
    path('categories/', ListeCategories.as_view(), name='liste_categories'),
    path('categories/ajouter/', AjouterCategorie.as_view(), name='ajouter_categorie'),
    path('categories/modifier/<int:pk>/', ModifierCategorie.as_view(), name='modifier_categorie'),
    path('categories/supprimer/<int:pk>/', SupprimerCategorie.as_view(), name='supprimer_categorie'),
    path('categories/<int:pk>/', JeuxParCategorie.as_view(), name='jeux_par_categorie'),

    # Éditeurs
    path('editeurs/', ListeEditeurs.as_view(), name='liste_editeurs'),  # ✅ AJOUTÉ

    # Joueurs
    path('joueurs/', ListeJoueurs.as_view(), name='liste_joueurs'),
    path('joueurs/ajouter/', AjouterJoueur.as_view(), name='ajouter_joueur'),
    path('joueurs/modifier/<int:pk>/', ModifierJoueur.as_view(), name='modifier_joueur'),
    path('joueurs/supprimer/<int:pk>/', SupprimerJoueur.as_view(), name='supprimer_joueur'),

    # Commentaires
    path('commentaires/', ListeCommentaires.as_view(), name='liste_commentaires'),
    path('commentaires/ajouter/', AjouterCommentaire.as_view(), name='ajouter_commentaire'),
    path('commentaires/modifier/<int:pk>/', ModifierCommentaire.as_view(), name='modifier_commentaire'),
    path('commentaires/supprimer/<int:pk>/', SupprimerCommentaire.as_view(), name='supprimer_commentaire'),

    # Editeurs
    path('editeurs/', ListeEditeurs.as_view(), name='liste_editeurs'),
    path('editeurs/ajouter/', AjouterEditeur.as_view(), name='ajouter_editeur'),
    path('editeurs/modifier/<int:pk>/', ModifierEditeur.as_view(), name='modifier_editeur'),
    path('editeurs/supprimer/<int:pk>/', SupprimerEditeur.as_view(), name='supprimer_editeur'),
    path('editeurs/', ListeEditeurs.as_view(), name='liste_editeurs'),
    path('editeurs/modifier/<int:pk>/', ModifierEditeur.as_view(), name='modifier_editeur'),

]
