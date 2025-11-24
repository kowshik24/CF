def kire(digits):
    final_date = "01032025"
    count = {}
    
    
    for d in digits:
        d = str(d)
        count[d] = count.get(d, 0) + 1
    
    for digit in final_date:
        if digit not in count or count[digit] == 0:
            return False
        count[digit] -= 1
    return True

def kor():
    n = int(input())
    nums = list(map(int, input().split()))
    
   
    for i in range(1, n + 1):
        prefix = nums[:i]
        if kire(prefix):
            return i
    return 0

def main():
    t = int(input())
    for _ in range(t):
        print(kor())

if __name__ == "__main__":
    main()
