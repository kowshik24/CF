def solve(n, a, s):
    max_score = 0
    i = 0
    
    while i < n:
        if s[i] == 'L':
            j = i + 1
            while j < n and s[j] != 'R':
                j += 1
            if j < n and s[j] == 'R':
                max_score += sum(a[i:j+1])
                i = j + 1
            else:
                i += 1
        else:
            i += 1

    i = n - 1
    max_score_2 = 0

    while i >= 0:
        if s[i] == 'R':
            j = i - 1
            while j >= 0 and s[j] != 'L':
                j -= 1
            if j >= 0 and s[j] == 'L':
                max_score_2 += sum(a[j:i+1])
                i = j - 1
            else:
                i -= 1
        else:
            i -= 1
    
    

    # Replace some 'R' with 'L' and vice versa

    max_score_3 = 0

    arr = []

    for i in range(n):
        if s[i] == 'R':
            arr.append(a[n - i - 1]-a[i])
        else:
            arr.append(a[i]-a[n - i - 1])

    arr.sort(reverse=True)
    for i in range(n):
        if arr[i] > 0:
            max_score_3 += arr[i]

    print(max_score, max_score_2, max_score_3)


    return max(max_score, max_score_2)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input().strip()
    print(solve(n, a, s))