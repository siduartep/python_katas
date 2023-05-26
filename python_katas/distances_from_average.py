def distances_from_average(data):
    average = get_average(data)
    return [element - average[0] for element in data]


def get_average(numbers):
    total = sum(numbers)
    lenght = len(numbers)
    average = total / lenght
    rounded = round(average, 2)
    return [rounded]
