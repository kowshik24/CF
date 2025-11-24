t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    from collections import Counter
    count = Counter(a)
    
    score = 0
    for value in count.values():
        score += value // 2

    print(score)