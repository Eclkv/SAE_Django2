# Generated by Django 5.2 on 2025-06-12 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='auteurs/')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('annee_sortie', models.PositiveIntegerField()),
                ('photo_boite', models.ImageField(blank=True, null=True, upload_to='jeux/')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.auteur')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.categorie')),
                ('editeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.editeur')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='gestion.jeu')),
                ('joueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.joueur')),
            ],
        ),
    ]
