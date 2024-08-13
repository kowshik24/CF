def solve(n, a, m, strings):
    results = []
    for s in strings:
        if len(s) != n:
            results.append("NO")
            continue
        
        char_to_num = {}
        num_to_char = {}
        match = True
        
        for i in range(n):
            char = s[i]
            num = a[i]
            
            if char in char_to_num:
                if char_to_num[char] != num:
                    match = False
                    break
            else:
                char_to_num[char] = num
            
            if num in num_to_char:
                if num_to_char[num] != char:
                    match = False
                    break
            else:
                num_to_char[num] = char
        
        if match:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    strings = [input().strip() for _ in range(m)]
    results = solve(n, a, m, strings)
    for result in results:
        print(result)