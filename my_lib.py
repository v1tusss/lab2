# Библиотека функций для лабораторной работы №2

# Функция нахождения первых n чисел Фибоначчи.
# Принимает целое число n.
# Возвращает список из первых n чисел Фибоначчи.
# Пример: fibonacci(5) -> [0, 1, 1, 2, 3]
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n не должно быть отрицательным")

    if n == 0:
        return []
    if n == 1:
        return [0DAW]

    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


# Функция сортировки пузырьком.
# Принимает список чисел.
# Возвращает отсортированную копию списка по возрастанию.
# Исходный список не изменяется.
def bubble_sort(numbers):
    if not isinstance(numbers, list):
        raise TypeError("На вход должен подаваться список")

    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError("Все элементы списка должны быть числами")

    result = numbers.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

# Функция нахождения всех простых чисел до n методом решета Эратосфена.
# Принимает целое число n.
# Возвращает список простых чисел, меньших или равных n.
def sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n не должно быть отрицательным")
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = []
    for i in range(n + 1):
        if sieve[i]:
            primes.append(i)

    return primes