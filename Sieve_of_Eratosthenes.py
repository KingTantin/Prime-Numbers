import time

def sieve(n):
    nums = [True for i in range(n+1)]
    nums[0] = nums[1] = False


    for possible_prime in range(2, int(n**(1/2))+1):        
        if nums[possible_prime]:
            for i in range(possible_prime**2, n+1, possible_prime):
                nums[i] = False

    primes = []
    for i, is_prime in enumerate(nums):
        if is_prime:
            primes.append(i)
    return primes


start = time.time()
primes = sieve(100)
end = time.time()

print(primes)
print(f'time: {end-start}')
print(f'num_of_primes_found: {len(primes)}')
