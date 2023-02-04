def check_if_pre_inaugaration(release_date):
    if release_date[1] == 1:
        if release_date[2] == 20:
            return "idk"
        return release_date[2] < 20
    return False

def invert(boolean):
    if boolean == "idk":
        return "idk"
    return not boolean

def check_if_obama(release_date):
    if 2009 <= release_date[0] and release_date[0] <= 2017:
        if release_date[0] == 2009:
            return invert(check_if_pre_inaugaration(release_date))
        if release_date[0] == 2017:
            return check_if_pre_inaugaration(release_date)
        return True
    return False
