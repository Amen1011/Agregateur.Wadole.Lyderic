from article import Article
from scraper import SiteScraper

class AgregateurNews:
    def __init__(self, mots_cles):
        self.mots_cles = mots_cles
        self.scrapers = []
        self.articles = []

    def ajouter_source(self, url):
        self.scrapers.append(SiteScraper(url, self.mots_cles))

    def collecter(self):
        self.articles = []
        for scraper in self.scrapers:
            resultats = scraper.extraire_titres()
            print(f"[DEBUG] {scraper.url} → {len(resultats)} articles trouvés")
            for titre, lien in resultats:
                self.articles.append(Article(titre, lien, scraper.url))
        print(f"[DEBUG] TOTAL : {len(self.articles)}")
        return self.articles
    
    def afficher_articles(self) :
        if not self.articles :
            print("Aucun article trouvé")
        else :
            for i, article in enumerate(self.articles, start = 1 ):
                print(f"{i} {article.titre} ({article.source}) -> {article.lien}")