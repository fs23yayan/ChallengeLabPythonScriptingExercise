def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Find primes between 1 and 250
primes = [str(num) for num in range(1, 251) if is_prime(num)]

# Write to results.txt
with open("results.txt", "w") as file:
    file.write("\n".join(primes))

# Verification Step: Read back and check
with open("results.txt", "r") as file:
    content = file.read().splitlines()
    content_primes = list(map(int, content))

# Expected primes for verification
expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                   61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                   131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                   197, 199, 211, 223, 227, 229, 233, 239, 241]

# Test if the result is as expected
if content_primes == expected_primes:
    print("✅ Test Passed: results.txt contains the correct list of prime numbers.")
else:
    print("❌ Test Failed: Mismatch in prime numbers list.")
