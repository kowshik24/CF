import sys

def kor():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n, m = int(data[index]), int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + m]))
        index += m
        
        
        arr1 = []
        j = 0

        for x in b:
            while j < n and a[j] < x:
                j += 1
            if j >= n:
                break
            arr1.append(j)
            j += 1
            # print(f"j: {j}")
        if len(arr1) == m:
            print(0)
            continue
        
        
        arr2 = [-1] * m
        j = n - 1

        for i in range(m-1, -1, -1):
            while j >= 0 and a[j] < b[i]:
                j -= 1
            if j < 0:
                break
            arr2[i] = j
            j -= 1
        
        
        arr3 = [False] * (m + 1)
        arr3[m] = True

        for i in range(m-1, -1, -1):
            if arr2[i] != -1 and arr3[i+1]:
                arr3[i] = True
            else:
                arr3[i] = False
        

        # print(f"arr1: {arr1}")
        # print(f"arr2: {arr2}")
        # print(f"arr3: {arr3}")
        res = []
        
        
        for i in range(m + 1):
            if i == 0:
                if m == 1:
                    res.append(b[0])
                else:
                    if arr3[1] and arr2[1] != -1:
                        res.append(b[0])
                        # print(f"arr2[1]: {arr2[1]}")
            elif i == m:
                if len(arr1) >= m-1:
                    # res.append(b[m])
                    res.append(b[m-1])
            else:
                if i-1 >= len(arr1):
                    continue
                p = arr1[i-1]
                if i+1 >= m:
                    res.append(b[i])
                else:
                    if arr3[i+1] and arr2[i+1] > p:
                        res.append(b[i])
        
        # print(f"res: {res}")
        if res:
            print(min(res))
        else:
            print(-1)

if __name__ == "__main__":
    kor()