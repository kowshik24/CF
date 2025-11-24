def check_kor(s):
    return s < s[::-1]

def kire(s, k):
    n = len(s)
    if n == 1:
        return False
    
    if check_kor(s):
        return True
    
    if k == 0:
        return False

    
    if s == s[::-1]:
        return k >= 1 and len(set(s)) > 1
    
    
    if len(set(s)) > 1:
        if k >= 1:
            for i in range(n):
                for j in range(i + 1, n):
                    final_list = list(s)
                    final_list[i], final_list[j] = final_list[j], final_list[i]
                    if check_kor(''.join(final_list)):
                        return True
    
    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    print("YES" if kire(s, k) else "NO")
