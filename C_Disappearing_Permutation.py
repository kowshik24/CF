import sys

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        p = list(map(int, data[ptr:ptr + n]))
        ptr += n
        d = list(map(int, data[ptr:ptr + n]))
        ptr += n
        
        # Compute p_inv (1-based)
        p_inv = [0] * (n + 1)
        for idx in range(n):
            val = p[idx]
            p_inv[val] = idx + 1  # 1-based position
        
        # Precompute pos_in_d (0-based index for each element in d)
        pos_in_d = [0] * (n + 1)
        for i in range(n):
            val = d[i]
            pos_in_d[val] = i  # 0-based index
        
        # Initialize delta array for prefix sum processing
        delta = [0] * (n + 2)  # 1-based steps up to n
        for j in range(n):
            x = d[j]
            y = p_inv[x]
            if y < 1 or y > n:
                # This should not happen as per problem constraints
                continue
            if pos_in_d[y] == 0 and d[0] != y:
                # Check if y is present in d
                y_in_d = False
                for k in range(n):
                    if d[k] == y:
                        y_in_d = True
                        break
                if not y_in_d:
                    start = j + 1
                    end = n
                    delta[start] += 1
                    if end + 1 <= n + 1:
                        delta[end + 1] -= 1
                else:
                    k = pos_in_d[y]
                    if k > j:
                        start = j + 1
                        end = k
                        delta[start] += 1
                        delta[end + 1] -= 1
            else:
                k = pos_in_d[y] if 1 <= y <= n else -1
                if k == -1:
                    start = j + 1
                    end = n
                    delta[start] += 1
                    if end + 1 <= n + 1:
                        delta[end + 1] -= 1
                else:
                    if k > j:
                        start = j + 1
                        end = k
                        delta[start] += 1
                        delta[end + 1] -= 1
        
        # Compute prefix sums to get count for each step
        count = [0] * (n + 1)  # 1-based steps
        current = 0
        for i in range(1, n + 1):
            current += delta[i]
            count[i] = current
        
        # Prepare the answer
        ans = []
        for i in range(1, n + 1):
            res = i + count[i]
            ans.append(str(res))
        results.append(' '.join(ans))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()