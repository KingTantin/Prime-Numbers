from math import isqrt

def prime_factorization(n: int) -> list:
    if n < 2:
        return [] 
    for num in range(2, int(isqrt(n)+1)):
        if n % num == 0:
            return [num] + prime_factorization(n//num)
    return [n]


def compactor(factors: list[int]) -> list[str]:
    counter_dict = {num: 0 for num in sorted(factors)}
    for num in factors:
        counter_dict[num] += 1
    return [f'{element}^{counter_dict[element]}'  for element in counter_dict]

n = 100000032412
x = prime_factorization(n)
print(compactor(x))
