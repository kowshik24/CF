
def kor():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        baki_ase = list(range(1, n + 1))
        kos = []
        for i in reversed(s):
            if i == '<':
                temp = baki_ase.pop(0)
            else:
                temp = baki_ase.pop()
            kos.insert(0, temp)
    
        kos.insert(0, baki_ase[0])
        print(' '.join(map(str, kos)))


if __name__ == "__main__":
    kor()