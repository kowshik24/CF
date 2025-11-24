def is_prime(x):
    
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def construct_permutation(t, test_cases):
    results = []
    for n in test_cases:
        if n == 3:
            
            results.append("-1")
            continue

       
        odd = [i for i in range(1, n + 1) if i % 2 != 0]
        even = [i for i in range(1, n + 1) if i % 2 == 0]
        permutation = even + odd

       
        is_valid = True
        for i in range(len(permutation) - 1):
            if is_prime(permutation[i] + permutation[i + 1]):
                is_valid = False
                break

        if is_valid:
            results.append(" ".join(map(str, permutation)))
        else:
            results.append("-1")
    
    return results


t = int(input())
test_cases = [int(input()) for _ in range(t)]


results = construct_permutation(t, test_cases)
print("\n".join(results))
