from flask import Flask, render_template, request
import feedparser
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    articles = []

    if query:
        # Google News cherche n'importe quel mot-clé
        url = f"https://news.google.com/rss/search?q={quote(query)}&hl=fr&gl=FR&ceid=FR:fr"
        feed = feedparser.parse(url)

        for entry in feed.entries:
            titre = entry.get("title", "")
            lien = entry.get("link", "")
            source = entry.get("source", {}).get("title", "Google News")

            articles.append({
                "titre": titre,
                "url": lien,
                "source": source
            })

    return render_template("index.html", articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)