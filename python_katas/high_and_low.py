def high_and_low(numbers):
    num_ls = numbers.split()
    numbers = [int(num) for num in num_ls]
    max_v = max(numbers)
    min_v = min(numbers)
    numbers = f"{max_v} {min_v}"
    return numbers
