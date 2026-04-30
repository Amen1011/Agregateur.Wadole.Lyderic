from agregateur import AgregateurNews
from storage import StorageJSON

print("1. Création de l'agrégateur...")
mon_agregrateur = AgregateurNews(["Guerre","Elections"])

print("2. Ajouter des sources...")
mon_agregrateur.ajouter_source("https://exemple-site1.com")
mon_agregrateur.ajouter_source("https://exemple-site2.com")

print("3. Collecte des titres...")
resultat = mon_agregrateur.collecter_tous_les_titres()
print(f"4. Resultat de la collecte : {resultat}")

print("5. Affichage des articles...")
mon_agregrateur.afficher_articles()

#sauvegarde 
StorageJSON.sauvegarder(mon_aggregateur.articles)

#chargement pour un nouveau programme
nouveaux_articles = StorageJSON.charger()

print("6. Fin du programme")