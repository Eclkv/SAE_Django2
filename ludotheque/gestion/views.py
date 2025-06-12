from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Jeu, Auteur, Categorie, Joueur, Commentaire, Editeur
from .forms import JeuForm
from .models import Editeur
# Vues génériques de base
class ListeGenerique(ListView):
    template_name = 'gestion/liste.html'

class FormulaireGenerique(CreateView):
    template_name = 'gestion/formulaire.html'
    success_url = reverse_lazy('liste_jeux')

class ModifierGenerique(UpdateView):
    template_name = 'gestion/formulaire.html'
    success_url = reverse_lazy('liste_jeux')

class SupprimerGenerique(DeleteView):
    template_name = 'gestion/confirm_delete.html'
    success_url = reverse_lazy('liste_jeux')

# -------------------------------
# CRUD Jeux
class ListeJeux(ListView):
    model = Jeu
    template_name = 'gestion/jeu_list.html'

class AjouterJeu(FormulaireGenerique):
    model = Jeu
    form_class = JeuForm

class ModifierJeu(ModifierGenerique):
    model = Jeu
    fields = '__all__'

class SupprimerJeu(SupprimerGenerique):
    model = Jeu

# Nouvelle vue pour la fiche détaillée d’un jeu
class FicheJeu(DetailView):
    model = Jeu
    template_name = 'gestion/fiche_jeu.html'
    context_object_name = 'jeu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentaires'] = Commentaire.objects.filter(jeu=self.object)
        return context

# -------------------------------
# CRUD Auteurs
class ListeAuteurs(ListeGenerique):
    model = Auteur

class AjouterAuteur(FormulaireGenerique):
    model = Auteur
    fields = '__all__'

class ModifierAuteur(ModifierGenerique):
    model = Auteur
    fields = '__all__'

class SupprimerAuteur(SupprimerGenerique):
    model = Auteur

# -------------------------------
# CRUD Catégories
class ListeCategories(ListeGenerique):
    model = Categorie

class AjouterCategorie(FormulaireGenerique):
    model = Categorie
    fields = '__all__'

class ModifierCategorie(ModifierGenerique):
    model = Categorie
    fields = '__all__'

class SupprimerCategorie(SupprimerGenerique):
    model = Categorie

# -------------------------------
# CRUD Joueurs
class ListeJoueurs(ListeGenerique):
    model = Joueur

class AjouterJoueur(FormulaireGenerique):
    model = Joueur
    fields = '__all__'

class ModifierJoueur(ModifierGenerique):
    model = Joueur
    fields = '__all__'

class SupprimerJoueur(SupprimerGenerique):
    model = Joueur

# -------------------------------
# CRUD Commentaires
class ListeCommentaires(ListeGenerique):
    model = Commentaire

class AjouterCommentaire(FormulaireGenerique):
    model = Commentaire
    fields = '__all__'

class ModifierCommentaire(ModifierGenerique):
    model = Commentaire
    fields = '__all__'

class SupprimerCommentaire(SupprimerGenerique):
    model = Commentaire

# -------------------------------
# Vue pour afficher les jeux d'une catégorie
class JeuxParCategorie(ListView):
    template_name = 'gestion/jeux_par_categorie.html'
    context_object_name = 'jeux'

    def get_queryset(self):
        self.categorie = get_object_or_404(Categorie, pk=self.kwargs['pk'])
        return Jeu.objects.filter(categorie=self.categorie)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorie'] = self.categorie
        return context


class AccueilView(TemplateView):
    template_name = 'gestion/accueil.html'


class ListeEditeurs(ListeGenerique):
    model = Editeur

class AjouterEditeur(FormulaireGenerique):
    model = Editeur
    fields = '__all__'

class ModifierEditeur(ModifierGenerique):
    model = Editeur
    fields = '__all__'

class SupprimerEditeur(SupprimerGenerique):
    model = Editeur

class ListeEditeurs(ListeGenerique):
    model = Editeur

class ModifierEditeur(UpdateView):
    model = Editeur
    fields = '__all__'
    template_name = 'gestion/formulaire.html'
    success_url = reverse_lazy('liste_editeurs')