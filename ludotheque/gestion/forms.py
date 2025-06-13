from django import forms
from .models import Jeu, Auteur, Categorie, Editeur

class JeuForm(forms.ModelForm):
    # Auteur
    auteur_existant = forms.ModelChoiceField(
        queryset=Auteur.objects.all(),
        required=False,
        label="Auteur existant"
    )
    auteur_nom = forms.CharField(required=False, label="Nom nouvel auteur")
    auteur_prenom = forms.CharField(required=False, label="Prénom nouvel auteur")
    auteur_age = forms.IntegerField(required=False, label="Âge nouvel auteur", min_value=0)

    # Catégorie
    categorie_existant = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=False,
        label="Catégorie existante"
    )
    nouvelle_categorie = forms.CharField(required=False, label="Nouvelle catégorie")

    # Éditeur
    editeur_existant = forms.ModelChoiceField(
        queryset=Editeur.objects.all(),
        required=False,
        label="Éditeur existant"
    )
    editeur_nom = forms.CharField(required=False, label="Nom nouvel éditeur")

    class Meta:
        model = Jeu
        fields = ['titre', 'annee_sortie', 'photo_boite']

    def clean(self):
        cleaned_data = super().clean()

        # Auteur
        if not cleaned_data.get('auteur_existant') and not (
            cleaned_data.get('auteur_nom') and cleaned_data.get('auteur_prenom') and cleaned_data.get('auteur_age')
        ):
            raise forms.ValidationError("Veuillez sélectionner un auteur existant ou en créer un.")

        # Catégorie
        if not cleaned_data.get('categorie_existant') and not cleaned_data.get('nouvelle_categorie'):
            raise forms.ValidationError("Veuillez sélectionner ou créer une catégorie.")

        # Éditeur
        if not cleaned_data.get('editeur_existant') and not cleaned_data.get('editeur_nom'):
            raise forms.ValidationError("Veuillez sélectionner ou créer un éditeur.")

        return cleaned_data

    def save(self, commit=True):
        # Auteur
        if self.cleaned_data['auteur_existant']:
            auteur = self.cleaned_data['auteur_existant']
        else:
            auteur = Auteur.objects.create(
                nom=self.cleaned_data['auteur_nom'],
                prenom=self.cleaned_data['auteur_prenom'],
                age=self.cleaned_data['auteur_age']
            )

        # Catégorie
        if self.cleaned_data['categorie_existant']:
            categorie = self.cleaned_data['categorie_existant']
        else:
            categorie, _ = Categorie.objects.get_or_create(nom=self.cleaned_data['nouvelle_categorie'])

        # Éditeur
        if self.cleaned_data['editeur_existant']:
            editeur = self.cleaned_data['editeur_existant']
        else:
            editeur, _ = Editeur.objects.get_or_create(nom=self.cleaned_data['editeur_nom'])

        jeu = super().save(commit=False)
        jeu.auteur = auteur
        jeu.categorie = categorie
        jeu.editeur = editeur

        if commit:
            jeu.save()
        return jeu
class JeuEditForm(forms.ModelForm):
    class Meta:
        model = Jeu
        fields = ['titre', 'annee_sortie', 'photo_boite', 'categorie', 'auteur', 'editeur']
