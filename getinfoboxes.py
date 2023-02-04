def parse(string):
    results = []
    depth = -1
    current = ""
    for char in string:
        if char == "{":
            depth += 1
        if depth > 0:
            current += char
        if char == "}":
            depth -= 1
            if depth == 0:
                results.append(current)
                current = ""
    return results

def find_sections_with(search, string):
    found_sections = []
    working_sections = parse("{{" + string + "}}")
    while working_sections:
        working_section = working_sections.pop()
        new_sections = []
        total_count_inside = 0
        for candidate in parse(working_section):
            count_in_candidate = candidate.count(search)
            if count_in_candidate > 0:
                new_sections.append(candidate)
                total_count_inside += count_in_candidate
        if working_section.count(search) > total_count_inside:
            found_sections.append(working_section)
        else:
            working_sections += new_sections
    found_sections.reverse()
    return found_sections

def get_infoboxes(string):
    return find_sections_with("Infobox", string)
