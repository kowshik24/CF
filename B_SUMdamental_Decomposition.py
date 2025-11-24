import sys

def count_kor(num):
    return bin(num).count('1')

def kor(y):
    if y == 0:
        return 2
    
    k = count_kor(y)
    if k >= 2:
        return y
    else: 
        if y == 1:
            return 5
        else:
            return y + 2


def ber_kor(K):
  if K < 2: return -1

  return K if K % 2 == 0 else K - 1


def ber_kor_odd(K):

  if K < 1: return -1
  
  return K if K % 2 == 1 else K - 1

def solve():
    
    n, x = map(int, sys.stdin.readline().split())

    
    if n == 1:
        
        if x == 0:
            print("-1") 
        else:
            print(x)   
        return

    
    k0 = count_kor(x) 

    if k0 >= n:
        print(x)
        return

    
    res = x ^ ((n - 2) % 2)
    res1 = (n - 2) + kor(res)

   
    
    res2 = float('inf') 
    y0 = x
    y1 = x ^ 1
    k1 = count_kor(y1)

    if n % 2 == 0: 
        
        cnt = ber_kor(k0)
        
        if cnt != -1:
            
            res2 = min(res2, n - cnt + y0)
            
        
        cnt1 = ber_kor_odd(k1)
        
        if cnt1 != -1:
             
             res2 = min(res2, n - cnt1 + y1)
             
    else: 
        cnt = ber_kor(k1)
        if cnt != -1:
             res2 = min(res2, n - cnt + y1)

        
        cnt1 = ber_kor_odd(k0)
        if cnt1 != -1:
             res2 = min(res2, n - cnt1 + y0)

    
    if res2 == float('inf'):
         print(res1)
    else:
         
         print(min(res1, res2))



if __name__ == "__main__":
    t = int(sys.stdin.readline())

    for _ in range(t):
        solve()