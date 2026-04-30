import json
from article import Article

class StorageJSON :
    @staticmethod
    def sauvegarder(articles, nom_fichier="article.json") :
        donnees = []
        for article in articles:
            donnees.append({
                 "titre": article.titre,
                "url": article.url,
                "source": article.source
            })
        
        with open (nom_fichier, "w", encoding = "utf-8") as f:
            json.dump(donnee, f, ensure_ascii = false, indent = 4)

        print(f"{len(donnees)} articles sauvegardés dans {nom_fichier}")

    @staticmethod
    def charger(nom_fichier = "articles.json") :
        article = []
        try :
            with open(nom_fichier, "r", encoding = "utf-8") as f :
                donnees = json.load(f)
            
            for item in donnees : 
                article = Article(item["titre"], item["url"], item["source"])
                article.append(article)
            
            print(f"{len(articles)} articles chargés depuis {nom_fichier}")
        except FileNotFoundError :
            print(f"Fichier {nom_fichier} non trouvé")
        
        return articles