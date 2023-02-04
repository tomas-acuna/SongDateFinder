import date

def get_release_date(infobox):
    return date.get_date(infobox.split("released", 1)[1].strip().split("=", 1)[1].split("\\n|", 1)[0])
