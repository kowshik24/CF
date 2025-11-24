import sys

def ber_kor(x):

    if x == 1:
        return 0
    else:
        length = (x-1).bit_length()
        # print(length)
        return length
    

def kor():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx+1])
        a = int(input[idx+2])
        b = int(input[idx+3])
        idx +=4
        
        k = min(a, n - a + 1)
        l = min(b, m - b + 1)

        # print(k, l)
        # cnt = 1 + ber_kor(n) + ber_kor(k)
        
        cnt = 1 + ber_kor(k) + ber_kor(m)
        cnt1 = 1 + ber_kor(n) + ber_kor(l)
        # print(cnt, cnt1)
        # if cnt == 1 and cnt1 == 1:
        #     ans = 0
        # else:
        #     ans = min(cnt, cnt1)
        
        ans = min(cnt, cnt1)
        print(ans)

if __name__ == "__main__":
    kor()