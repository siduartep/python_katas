def high_and_low(numbers_str):
    num_ls = numbers_str.split()
    numbers = [int(num) for num in num_ls]
    max_value = max(numbers)
    min_value = min(numbers)
    return f"{max_value} {min_value}"
