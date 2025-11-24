import sys

input = sys.stdin.readline

def kor():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[arr[i]] = i + 1
        
    results = []

    for _ in range(q):
        l, r, k = map(int, input().split())
        
        if k < 1 or k > n:
            results.append("-1")
            continue
            
        indx = pos[k]
        
        if indx < l or indx > r:
            results.append("-1")
            continue

        temp, temp1 = l, r
        index = []
        flag = False

        while temp <= temp1:
            m = (temp + temp1) // 2
            # print(f"m: {m}")
            index.append(m)
            
            if m == indx:
                flag = True
                break
                
            if indx < m:
                temp1 = m - 1
            else:
                temp = m + 1
            # print(f"temp: {temp}")
            # print(f"temp1: {temp1}")
            # print(f"index: {index}")
        
        if not flag:
            results.append("-1")
            continue

        kos = set(index[:-1])
        # print(f"kos: {kos}")
        S = set()
        
        for i in kos:
            num = arr[i-1]
            
            if indx > i:
                if num >= k:
                    S.add(i)
            elif indx < i:
                if num <= k:
                    S.add(i)

        baki_ase = 0
        baki_ase1 = 0
        
        for i in S:
            if indx > i:
                baki_ase += 1
            else:
                baki_ase1 += 1

        cnt = 0
        cnt1 = 0
        
        for i in S:
            num1 = arr[i-1]
            if num1 < k:
                cnt += 1
            elif num1 > k:
                cnt1 += 1

        # num3 = min(0, baki_ase - cnt)
        # num4 = max(0, baki_ase1 - cnt1 + 1)


        num3 = max(0, baki_ase - cnt)
        num4 = max(0, baki_ase1 - cnt1)

        # print("num3:", num3)
        # print("num4:", num4)

        P = kos.copy()
        P.add(indx)

        num5 = 0
        num6 = 0
        
        # for i in P:
        #     if 1 <= i <= n:
        #         kire = arr[i-1]
        #         if kire > k:
        #             num5 += 1
        #         elif kire < k:
        #             num6 += 1


        # print(f"P: {P}")
        # print(f"num5: {num5}")
        # print(f"num6: {num6}")

        for i in P:
            if 1 <= i <= n:
                kire = arr[i-1]
                if kire < k:
                    num5 += 1
                elif kire > k:
                    num6 += 1


        # num7 = k - num5
        # num8 = n - num6

        num7 = (k - 1) - num5
        num8 = (n - k) - num6
        # print(f"num7: {num7} num8: {num8}")

        if (num7 >= num3) and (num8 >= num4):
            kos2 = num3 + num4
            # print("eikhane")
            # print(f"kos2: {kos2}")
            # if kos2 <= len(S):
            #     kos3 = len(S) - kos2
            #     # print(f"kos3: {kos3}")
            #     results.append(str(kos3))
            # else:
            #     results.append("-1")
            kos3 = len(S) + kos2
            results.append(str(kos3))
        else:
            results.append("-1")

    print(" ".join(results))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        kor()