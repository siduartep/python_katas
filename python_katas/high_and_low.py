def high_and_low(numbers_str):
    num_ls = numbers_str.split()
    numbers = [int(num) for num in num_ls]
    max_v = max(numbers)
    min_v = min(numbers)
    return f"{max_v} {min_v}"
