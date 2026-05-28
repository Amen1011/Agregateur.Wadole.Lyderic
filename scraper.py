import re
import requests
from bs4 import BeautifulSoup


class SiteScraper:

    def __init__(self, url, mots_cles):
        self.url = url
        self.mots_cles = mots_cles

    def contient_mot_cle(self, texte):

        for mot in self.mots_cles:

            if re.search(
                rf"\b{re.escape(mot)}\b",
                texte,
                re.IGNORECASE
            ):
                return True

        return False

    def extraire_titres(self):

        try:

            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(
                self.url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            articles = []

            # Recherche des titres
            titres = soup.find_all(["h1", "h2", "h3"])

            print(
                f"[DEBUG] Titres trouvés sur {self.url} : {len(titres)}"
            )

            for t in titres:

                texte = t.get_text(strip=True)

                # Vérifie le texte
                if not texte:
                    continue

                # Vérifie mot-clé
                #if not self.contient_mot_cle(texte):
                #    continue

                lien = self.url

                # Cherche un lien dans le titre
                lien_tag = t.find("a", href=True)

                # Sinon cherche un parent <a>
                if not lien_tag:
                    lien_tag = t.find_parent("a")

                if lien_tag and lien_tag.has_attr("href"):

                    lien = lien_tag["href"]

                    # Corrige les liens relatifs
                    if lien.startswith("/"):

                        lien = self.url.rstrip("/") + lien

                #article = {
                #   "titre": texte,
                #    "lien": lien
                #}

                articles.append((texte, lien))

            print(
                f"[DEBUG] {self.url} → {len(articles)} articles trouvés"
            )

            return articles

        except Exception as e:

            print(f"[ERREUR] {self.url} : {e}")

            return []