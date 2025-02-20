# Exo 1
    # Les rapports financiers d'une entreprise sont stockés dans un fichier Excel : Structuré
    # Photographies téléchargées sur une plateforme de médias sociaux : Non structuré
    # Une collection d'articles d'information sur un site web : Non structuré
    # Données d'inventaire dans une base de données relationnelle : Structuré
    # Entretiens enregistrés dans le cadre d'une étude de marché : Non structuré

# Exo 2
# - Une série d'articles de blog sur les expériences de voyage : On peut créer un tableau avec ces colonnes : (Titre du message et Date)
# Sentiment (positif, négatif, neutre)
# Nous pouvons déterminer le sentiment en vérifiant les mots positifs/négatifs.

# - Enregistrements audio des appels du service client :
# Nous pouvons créer un tableau avec ces colonnes : Transcription, Date et Sentiment (Positif, Négatif, Neutre)
# Nous pouvons déterminer le sentiment en convertissant la parole en texte et en analysant les mots utilisés.

# - Notes manuscrites d'une séance de brainstorming :
# Nous pouvons convertir l'écriture manuscrite en texte, puis les organiser dans un tableau avec des colonnes pour le sujet, les idées clés, le contributeur et la date.

# Un tutoriel vidéo sur la cuisine :
# Nous pouvons transcrire la vidéo en texte et créer un tableau structuré avec ces colonnes : recette, Préparation, Ingrédients, cuisson.
# Cela facilite la recherche, le filtrage et l'analyse des tutoriels de cuisine.


!pip install pandas

import pandas as pd
train = pd.read_csv("train.csv")

train.head()

