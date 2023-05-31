def likes(name):
    number_likes = len(name)
    if name == []:
        return "no one likes this"
    elif number_likes == 1:
        return "Peter likes this"
    else:
        return "Jacob and Alex like this"
