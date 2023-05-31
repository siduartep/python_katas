def likes(name):
    number_likes = len(name)
    if number_likes == 0:
        return print_no_one()
    elif number_likes == 1:
        return f"{name[0]} likes this"
    elif number_likes == 2:
        return f"{name[0]} and {name[1]} like this"


def print_no_one():
    return "no one likes this"
