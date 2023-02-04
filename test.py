import getsong, obamadetector, date

def get_search_result(guess):
    song = getsong.get_song(guess)
    if song == "not found":
        return guess + "\nERROR could not find song"
    guess_title_date = guess + "\n" + song["title"] + "\n" + date.date_to_string(song["release_date"])
    obama = obamadetector.check_if_obama(song["release_date"])
    if obama == "idk":
        return guess_title_date + "\nMAYBE OBAMA "
    elif obama:
        return guess_title_date + "\nOBAMA"
    else:
        return guess_title_date + "\nNOT OBAMA"

print()
cont = True
while cont:
    search = input("search for song: ")
    if search == "exit":
        cont = False
    else:
        print(get_search_result(search))
        print()
