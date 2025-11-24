import sys


def kor():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    arr = []
    for i in range(n):
        arr.append((a[i], i + 1))

    arr.sort(key=lambda x: (-x[0], x[1]))
    p = [item[1] for item in arr]
    inx = set()
    cnt = 0

    if n == 0:
        print(0)
        return

    kos = p[0]
    cnt = 1
    inx.add(kos)

    for i in range(1, n):
        temp = p[i]

        left = (temp - 1) in inx

        right = (temp + 1) in inx
       
        if not left and not right:
            cnt += 1
        
        inx.add(temp)

    print(cnt)


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        kor()