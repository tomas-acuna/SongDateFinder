import re

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def get_year(date_string):
    year_strings = re.findall("[0-9][0-9][0-9][0-9]", date_string)
    if year_strings:
        return int(year_strings[0])
    return "idk"

def get_month(date_string):
    month = 0
    for month_name in month_names:
        month += 1
        if month_name in date_string:
            return month
    return "idk"

def get_day(date_string):
    date_string = re.sub("[0-9][0-9][0-9][0-9]", "", date_string)
    day_strings = re.findall("[0-9]+", date_string)
    if day_strings:
        return int(day_strings[0])
    return "idk"

def get_date(crude_date_string):
    date_string = re.sub("<ref.+</ref>", "", crude_date_string)
    proper_date_strings = re.findall("[0-9]+\|[0-9]+\|[0-9]+", date_string)
    if proper_date_strings:
        return list(map(int, proper_date_strings[0].split("|")))
    return [get_year(date_string), get_month(date_string), get_day(date_string)]

def year_or_day_to_string(n):
    if n == "idk":
        return ""
    return str(n)

def month_to_string(month):
    if month == "idk":
        return ""
    return month_names[month - 1]

def get_self(thing):
    return thing

def date_to_string(date):
    return " ".join(filter(get_self, [month_to_string(date[1]), year_or_day_to_string(date[2]), year_or_day_to_string(date[0])]))
