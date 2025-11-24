import math
import sys

def ber_kor(arr):
    if not arr:
        return 0
    temp = arr[0]
    for num in arr[1:]:
        temp = math.gcd(temp, num)
        if temp == 1:
            break
    return temp

def kire():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        m = min(a)
        num1 = [x for x in a if x % m == 0]
        num2 = [x for x in a if x % m != 0]
        
        if len(num2) > 0:
            count_kor = num1.count(m)
            if count_kor >= 2:
                print("Yes")
            else:
                baki_ase = [x // m for x in num1 if x != m]
                if not baki_ase:
                    print("No")
                else:
                    temp = ber_kor(baki_ase)
                    print("Yes" if temp == 1 else "No")
        else:
            count_kor = num1.count(m)
            if count_kor >= 2:
                print("Yes")
            else:
                baki_ase = [x // m for x in num1 if x != m]
                if not baki_ase:
                    print("No")
                else:
                    temp = ber_kor(baki_ase)
                    print("Yes" if temp == 1 else "No")

if __name__ == "__main__":
    kire()