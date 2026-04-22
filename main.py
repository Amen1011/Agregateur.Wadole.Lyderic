from agregateur import AgregateurNews
mon_agregrateur = AgregateurNews(["IA","Python"])
mon_agregrateur.ajouter_source("https://exemple-site1.com")
mon_agregrateur.ajouter_source("https://exemple-site2.com")
mon_agregrateur.collecter_tous_les_titres()
mon_agregrateur.afficher_articles()