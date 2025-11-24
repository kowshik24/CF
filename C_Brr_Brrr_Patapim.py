def kor():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        result = {}
        for i in range(n):
            for j in range(n):
                index = (i + 1) + (j + 1)
                if index not in result:
                    result[index] = arr[i][j]
        res = []
        for i in range(2, 2 * n + 1):
            res.append(result[i])

        kos = set(res)
        x = None
        for index in range(1, 2 * n + 1):
            if index not in kos:
                x = index
                break

        final_result = [x] + res
        print(' '.join(map(str, final_result)))

if __name__ == "__main__":
    kor()