def likes(name):
    number_likes = len(name)
    return printer[number_likes](name)


def print_four_or_more_people(name):
    number_likes = len(name)
    others = number_likes - 2
    return f"{name[0]}, {name[1]} and {others} others like this"


def print_three_people(name):
    return f"{name[0]}, {name[1]} and {name[2]} like this"


def print_two_people(name):
    return f"{name[0]} and {name[1]} like this"


def print_one_person(name):
    return f"{name[0]} likes this"


def print_no_one(name):
    return "no one likes this"


printer = [
    print_no_one,
    print_one_person,
    print_two_people,
    print_three_people,
    print_four_or_more_people,
]
