def likes(name):
    number_likes = len(name)
    is_one_person = number_likes == 0
    if is_one_person:
        return print_no_one(name)
    elif number_likes == 1:
        return print_one_person(name)
    elif number_likes == 2:
        return print_two_people(name)


def print_two_people(name):
    return f"{name[0]} and {name[1]} like this"


def print_one_person(name):
    return f"{name[0]} likes this"


def print_no_one(name):
    return "no one likes this"
