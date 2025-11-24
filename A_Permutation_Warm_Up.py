import sys

def kor():
    n = int(sys.stdin.readline())
    
    result = (n * n // 4) + 1

    print(result)

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        kor()