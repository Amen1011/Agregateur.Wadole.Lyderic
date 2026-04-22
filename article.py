class Article :
    def __init__(self, titre, url, source, date = None) :
        self.titre = titre
        self.url = url
        self.source = source
        self.date = date
    
    def __str__(self) :
        return f"{self.titre} ({self.source})"