import sys

def kor():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    res = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx + 1])
        idx += 2
        l = list(map(int, data[idx:idx + n]))
        idx += n
        r = list(map(int, data[idx:idx + n]))
        idx += n
        
        max_sum = 0
        kos = []
        
        for i in range(n):
            li = l[i]
            ri = r[i]
            max_sum += max(li, ri)
            # print(f"li: {li}, ri: {ri}, max_sum: {max_sum}")
            kos.append(min(li, ri))
        
        sum1 = max_sum + k

        # print(f"max_sum: {max_sum}, sum1: {sum1}")
        
        if k == 0:
            kire = 0
        else:
            temp = sorted(kos, reverse=True)
            kire = sum(temp[:k - 1])
            # print(f"kos: {temp}, kire: {kire}")
        
        sum2 = max_sum + kire + 1
        # print(f"sum1: {sum1}, sum2: {sum2}")
        res.append(max(sum1, sum2))
        # print(f"res: {res}")
    
    print('\n'.join(map(str, res)))

if __name__ == '__main__':
    kor()