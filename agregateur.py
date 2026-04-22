from article import Article 
from scraper import SiteScraper

class AgregateurNews :
    def __init__(self, mots_cles) :
        self.mots_cles = mots_cles
        self.scrapers = []
        self.articles = []

    def ajouter_source(self, url) :
        scraper = SiteScraper(url, self.mots_cles)
        self.scrapers.append(scraper)

    def collecter_tous_les_titres(self) :
        self.articles = []
        for scraper in self.scrapers :
            titres = scrapers.extraire_titres() : 
            for titre in titres :
                article = Article(titre, scraper.url, scraper.url)
                self.articles.append(article)
            
    def afficher_articles(self) :
        for article in self.articles :
            print(article)