from functions import average, normalize_text, select_numbers, sum_digits

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

a = [-5, 0, 2, 5]
assert select_numbers(a, 2) == []
assert select_numbers([], 2) == []
assert a == [-5, 0, 2, 5]

assert select_numbers([3, -3, 2, -2, 4, -4, 0], 2) == [3, -3]
assert select_numbers([3, 3, 1, -3], 2) == [3, 3, -3]
assert select_numbers([1, -1, 5], 0) == []

assert abs(average([1, 2]) - 1.5) < 1e-9
assert abs(average([1, 2, 4]) - 7 / 3) < 1e-9

print("Все проверки пройдены")
