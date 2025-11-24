import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        results.append(str(count_kor(n)))
    
    print('\n'.join(results))

def count_kor(n):
    if n <= 10**6:
        return kire_vai(n)
    else:
        return faster(n)

def kire_vai(n):
    is_prime = bytearray(n + 1)  
    count = 0
    
    for p in range(2, n + 1):
        if not is_prime[p]: 
            
            count += n // p
            
            
            j = p * p
            while j <= n:
                is_prime[j] = 1
                j += p
    
    return count

def faster(n):
    sqrt_n = int(n**0.5)
    
    
    check_kor = bytearray(sqrt_n + 1)
    primes = []
    
    for i in range(2, sqrt_n + 1):
        if not check_kor[i]:
            primes.append(i)
            j = i * i
            while j <= sqrt_n:
                check_kor[j] = 1
                j += i
    
    
    count = 0
    for p in primes:
        count += n // p
    
    
    size = 10**5
    
    for low in range(sqrt_n + 1, n + 1, size):
        high = min(low + size - 1, n)
        segment = bytearray(high - low + 1)
        
        
        for p in primes:
           
            start = (low + p - 1) // p * p
            if start < low:
                start += p
            
            
            for j in range(start, high + 1, p):
                segment[j - low] = 1
        
        
        for i in range(high - low + 1):
            if not segment[i] and low + i > 1:  
                count += 1  
    
    return count

if __name__ == "__main__":
    solve()