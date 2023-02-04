import urllib.request, urllib.parse, json

def get_text(url):
    with urllib.request.urlopen(url) as file:
        return file.read().decode()

def shrink_page(page):
    return dict((key, page[key]) for key in ["title", "pageid"])

def get_pages(guess):
    return list(map(shrink_page, json.loads(get_text("https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=" + urllib.parse.quote(guess)))["query"]["search"]))

def get_page_text(pageid):
    return get_text("https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&format=json&pageid=" + str(pageid))
