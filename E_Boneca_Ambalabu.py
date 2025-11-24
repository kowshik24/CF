import sys

def kor():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        cnt = [0] * 30
        for x in a:
            for j in range(30):
                if x & (1 << j):
                    cnt[j] += 1
        num1 = 0
        for x in a:
            temp = 0
            for j in range(30):
                if x & (1 << j):
                    temp += (n - cnt[j]) * (1 << j)
                else:
                    temp += cnt[j] * (1 << j)
            if temp > num1:
                num1 = temp
        results.append(num1)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    kor()