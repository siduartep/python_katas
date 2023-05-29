def distances_from_average(data):
    average = get_average(data)
    return resta_promedio_elemento(data, average)


def resta_promedio_elemento(data, average):
    return [average[0] - element for element in data]


def get_average(numbers):
    total = sum(numbers)
    lenght = len(numbers)
    average = total / lenght
    rounded = round(average, 2)
    return [rounded]
