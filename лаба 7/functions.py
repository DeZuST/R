def sum_digits(number):
    n = abs(number)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    return " ".join(text.lower().split())

def select_numbers(numbers, threshold):
    r = []
    for x in numbers:
        if threshold < abs(x) < threshold * 2:
            r.append(x)
    return r
