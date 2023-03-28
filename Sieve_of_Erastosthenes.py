def sieve(N: int) -> list[int]:
    numbers = [x for x in range(N + 1)]
    numbers[1] = 0
    for i in range(2 * 2, len(numbers), 2):
        numbers[i] = 0
    for i in range(3, len(numbers), 2):
        if numbers[i] != 0:
            for j in range(numbers[i] * 2, len(numbers), numbers[i]):
                numbers[j] = 0
    primes = [i for i in numbers if i != 0]
    return primes


if __name__ == '__main__':
    N = 1000
    print(sieve(N))
