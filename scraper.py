import re
import requests 
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class Scraper(ABC) :
    @abstractmethod
    def extraire_titres(self) :
        pass

class SiteScraper(Scraper) : 
    def __init__(self, url, mots_cles) :
        self.url = url
        self.mots_cles = mots_cles

    def contient_mot_cle(self, texte) :
        for mot in self.mots_cles :
            if re.search(rf'\b{re.escape(mot)}\b', texte, re.IGNORECASE):
                return True
        return False

    def extraire_titres(self) :
        try:
         headers={
            "User-Agent": "Mozilla/5.0(windows NT 10.0; Win64; x64)"
         }   
            reponse = requests.get(self.url,timeout=5)
            reponse.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

           articles = []

           titres=soup.find_all(["h1","h2","h3"])
           for t in titres:
            texte = t.get_text().strip()

            if text and self.continent_mot_cle(texte):
                lien_tag = t.find_parent("a")
                lien = lien_tag["href"] if lien_tag and lien_tag.has_attr("href") else self.url

                if lien.startswith("/"):
                   lien = self.url + lien 


                   articles.append((texte,lien))

            return articles


         except requests.exceptions.RequestException as e:
            print(f"ERREUR réseau pour {self.url}:",e)
            return[]

            except Exception as e:
                print("Erreur scraping:", e)

                return [] 