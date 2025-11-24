def mex(arr):
    s = set(arr)
    mex = 0
    while mex in s:
        mex += 1
    return mex

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        steps = []
        
        
        while len(a) > 1:
            
            if mex(a) == 0:
                steps.append((1, len(a)))
                a = [0]
                continue
            
            
            found = False
            for i in range(len(a)-1):
                for j in range(i+1, len(a)):
                    sub_arr = a[i:j+1]
                    if mex(sub_arr) == 0:
                        steps.append((i+1, j+1))
                        a = a[:i] + [0] + a[j+1:]
                        found = True
                        break
                if found:
                    break
            
            
            if not found:
                steps.append((1, 2))
                new_val = mex(a[:2])
                a = [new_val] + a[2:]
        
        print(len(steps))
        for l, r in steps:
            print(l, r)

if __name__ == "__main__":
    solve()