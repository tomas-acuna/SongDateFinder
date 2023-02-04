import wikipediastuff, getinfoboxes, getreleasedate

def get_song(guess):
    song = {}
    pages = wikipediastuff.get_pages(guess + " song")
    for page in pages:
        infoboxes = getinfoboxes.get_infoboxes(wikipediastuff.get_page_text(page["pageid"]))
        if infoboxes and "released" in infoboxes[0]:
            song["title"] = page["title"]
            song["release_date"] = getreleasedate.get_release_date(infoboxes[0])
            return song
    return "not found"
