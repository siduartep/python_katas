def likes(name):
    number_likes = len(name)
    is_no_one = number_likes == 0
    is_one_person = number_likes == 1
    is_two_people = number_likes == 2
    if is_no_one:
        return print_no_one(name)
    elif is_one_person:
        return print_one_person(name)
    elif is_two_people:
        return print_two_people(name)


def print_two_people(name):
    return f"{name[0]} and {name[1]} like this"


def print_one_person(name):
    return f"{name[0]} likes this"


def print_no_one(name):
    return "no one likes this"


def print_who_likes(print_function, name):
    pass
