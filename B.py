import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        x = int(data[idx+2])
        idx +=3
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        
        suffix_sum = [0] * n
        suffix_sum[-1] = a[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = a[i] + suffix_sum[i+1]
        ts = sum(a)
        
        ans = 0
        for i in range(n):
            si = suffix_sum[i]
            if si >= x:
                ans += k
            else:
                if ts == 0:
                    continue  # impossible since a has positive elements
                # Check if even taking all possible blocks is not enough
                total = si + (k-1)*ts
                if total < x:
                    continue
                delta = x - si
                m_part = (delta + ts - 1) // ts
                m_min = m_part + 1
                c_count = k - m_min + 1
                if c_count > 0:
                    ans += c_count
        print(ans)

if __name__ == "__main__":
    main()
