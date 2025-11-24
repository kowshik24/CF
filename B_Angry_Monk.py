def kor():

    t = int(input())
    for _ in range(t):
        n , k = map(int, input().split())
        arr = list(map(int, input().split()))
        sum = -1
        for i in range(k):
            sum = max(sum,arr[i])
        
        print(2 * (n-sum) - k + 1)

if __name__ == "__main__":
    kor()
