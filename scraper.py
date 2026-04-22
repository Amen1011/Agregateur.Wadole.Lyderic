import re
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
        titres_utilisateurs = [
            "Résumé du match Real Madrid vs Alavès",
            "Guerre en Iran",
            "Elections présidentielles au Bénin"
        ]

        resultats = []
        for titre in titres_utilisateurs :
            if self.contient_mot_cle(titre) :
                resultats.append(titre)
        
        return resultats
           