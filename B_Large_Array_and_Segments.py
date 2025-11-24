import sys

def kire():
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
        
        cum_sum = [0] * n
        cum_sum[-1] = a[-1]
        for i in range(n-2, -1, -1):
            cum_sum[i] = a[i] + cum_sum[i+1]
        ts = sum(a)
        
        ans = 0
        for i in range(n):
            si = cum_sum[i]
            if si >= x:
                ans += k
            else:
                if ts == 0:
                    continue  
                
                total = si + (k-1)*ts
                #print(f"si: {si}, total: {total}, ts: {ts}, k: {k}")
                if total < x:
                    continue
                baki_ase = x - si
                m_part = (baki_ase + ts - 1) // ts
                # print(m_part)
                m_min = m_part + 1
                # print("M min", m_min)
                c_count = k - m_min + 1
                if c_count > 0:
                    ans += c_count
        print(ans)

if __name__ == "__main__":
    kire()