import json

def sauvegarder(articles):
    data = []
    for a in articles:
        data.append({
            "titre": a.titre,
            "url": a.url,
            "source": a.source
        })

    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def charger():
    try:
        with open("articles.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []