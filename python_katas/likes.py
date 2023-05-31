def likes(name):
    number_likes = len(name)
    return selector[number_likes](name)


def print_three_people(name):
    return f"{name[0]}, {name[1]} and {name[2]} like this"


def print_two_people(name):
    return f"{name[0]} and {name[1]} like this"


def print_one_person(name):
    return f"{name[0]} likes this"


def print_no_one(name):
    return "no one likes this"


selector = {0: print_no_one, 1: print_one_person, 2: print_two_people, 3: print_three_people}
