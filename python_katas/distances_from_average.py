def distances_from_average(data):
    average = get_average(data)
    substraction = [average[0] - element for element in data]
    return substraction


def substract_average_to_element(data, average):
    return [average[0] - element for element in data]


def get_average(numbers):
    total = sum(numbers)
    lenght = len(numbers)
    average = total / lenght
    rounded = round(average, 2)
    return [rounded]
