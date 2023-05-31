def likes(name):
    number_likes = len(name)
    if name == []:
        return "no one likes this"
    elif number_likes == 1:
        return f"{name[0]} likes this"
    elif number_likes == 2:
        return f"{name[0]} and {name[1]} like this"
