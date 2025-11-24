import bisect

def kor():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        p = data[idx]
        idx += 1
        s = data[idx]
        idx += 1
        
        len1 = len(p)
        len2 = len(s)
        
        
        if len2 < len1 or len2 > 2 * len1:
            print("NO")
            continue
        
        
        L = []
        R = []
        for i, c in enumerate(s):
            if c == 'L':
                L.append(i)
            else:
                R.append(i)
        
        num1 = 0
        num2 = 0
        flag = True
        
        for c in p:
            if c == 'L':
                arr = L
            else:
                arr = R
            
           
            left = bisect.bisect_left(arr, num1)
            
            if left >= len(arr) or arr[left] > num2:
                flag = False
                break
            kos1 = arr[left]
            
            right = bisect.bisect_right(arr, num2) - 1
            if right < 0 or arr[right] < num1:
                flag = False
                break
            kos2 = arr[right]
            
            curr1 = kos1 + 1
            if kos2 + 1 < len2 and s[kos2 + 1] == c:
                curr2 = kos2 + 2
            else:
                curr2 = kos2 + 1
            
            num1 = curr1
            num2 = curr2
            
            if num1 > num2:
                flag = False
                break
        
        if flag and num1 <= len2 <= num2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    kor()