import sys
from collections import defaultdict


# def kor():
#     input = sys.stdin.read
#     data = input().split()
#     idx = 0
#     t = int(data[idx])
#     idx += 1
#     for _ in range(t):
#         n = int(data[idx])
#         idx += 1
#         s = data[idx]
#         idx += 1
        
#         arr = []
 
#         for i in range(n-1):
#             if s[i] != s[i+1]:
#                 arr.append(i)
#         kos = len(arr)
#         cnt = 1 if s[0] == '1' else 0
#         res1 = kos + cnt
 
#         # print(f"kos = {kos} cnt = {cnt} res1 = {res1}")
        
        
#         score = 0
#         for r in range(n):
#             tem = 1 if s[r] == '1' else 0
#             tem1 = tem - cnt
#             # print(f"tem = {tem} tem1 = {tem1}")
            
#             if r < n-1:
#                 kos2 = 1 if (s[r] != s[r+1]) else 0
#                 kos3 = 1 if (s[0] != s[r+1]) else 0
#                 baki_ase = kos3 - kos2
#                 # print(f"baki_ase = {baki_ase}")
#             else:
#                 baki_ase = 0
            
#             kire_vai = baki_ase + tem1
#             # print(f"kire_vai = {kire_vai} tem1 = {tem1} baki_ase = {baki_ase}")
#             if kire_vai < score:
#                 score = kire_vai
        
        
#         cnt_kor = defaultdict(int)
        
#         for i in arr:
#             temp = (s[i], s[i+1])
#             cnt_kor[temp] += 1
 
#         # print(cnt_kor)
 
#         flag = any(cnt >= 2 for cnt in cnt_kor.values())
        
#         score1 = 0
#         if flag:
#             score1 = -2
#         else:
            
#             score1 = 0
#             for i in range(len(arr) - 1):
#                 # a = arr[i+1]
#                 # b = arr[i-1]
#                 # A = s[a-1]
#                 # C = s[a+1]
#                 # B = s[b]
 
#                 a = arr[i]
#                 b = arr[i+1]
#                 A = s[a]
#                 C = s[a+1]
#                 B = s[b]
#                 if b + 1 < n:
#                     D = s[b+1]
#                 else:
#                     D = None
                
#                 kos4 = 1 if (A != B) else 0
#                 kos3 = 1 if (C != D) else 0 if D is not None else 0
                
#                 kos5 = 1  
#                 kos2 = 1 if (b + 1 < n and s[b] != s[b+1]) else 0
                
#                 baki_ase = (kos4 + kos3) - (kos5 + kos2)
#                 # print(f"{a} {b} {kos4} {kos3} {kos5} {kos2} {baki_ase} {score1}")
#                 if baki_ase < score1:
#                     score1 = baki_ase
        
#         final_res = min(score, score1)
#         # print(f"final_res = {final_res}")
#         res2 = res1 + final_res
#         res3 = n + res2
#         print(res3)

def kor():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        cnt = kos2 = kos3 = 0
        temp = '0'
        
        for i in s:
            if i != temp:
                cnt += 1
                if temp == '1':
                    kos3 += 1
                else:
                    kos2 += 1
            # print(f"i = {i} temp = {temp} cnt = {cnt} kos2 = {kos2} kos3 = {kos3}")
            temp = i
        
        res = 2 if (kos2 >= 2 or kos3 >= 2) else (1 if cnt >= 2 else 0)
        # print(f"res = {res}")
        
        res1 = cnt - res + n
    
        
        print(res1)

if __name__ == '__main__':
    kor()