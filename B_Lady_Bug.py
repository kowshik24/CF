import sys
input = sys.stdin.readline


def kire():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()
        
        counter1 = 0
        counter2 = 0
        
        
        counter3 = 0
        counter4 = 0
        
        for i in range(n):
            if (i % 2) == 0:  
                if a[i] == '1':
                    counter1 += 1
            else:  
                if a[i] == '1':
                    counter2 += 1
        
        
        for i in range(n):
            if (i % 2) == 0:  
                counter4 += 1
                if b[i] == '1':
                    counter2 += 1
            else:  
                counter3 += 1
                if b[i] == '1':
                    counter1 += 1
        
        
        if (counter2 <= counter4) and (counter1 <= counter3):
            res = "YES"
        else:
            res = "NO"

        print(res)



if __name__ == "__main__":
    kire()