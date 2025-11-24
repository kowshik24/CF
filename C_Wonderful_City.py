import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        h = []
        for _ in range(n):
            row = list(map(int, input[ptr:ptr+n]))
            h.append(row)
            ptr += n
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        b = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        # Check if original grid is beautiful
        beautiful = True
        # Check horizontal adjacents
        for i in range(n):
            for j in range(n-1):
                if h[i][j] == h[i][j+1]:
                    beautiful = False
        # Check vertical adjacents
        for j in range(n):
            for i in range(n-1):
                if h[i][j] == h[i+1][j]:
                    beautiful = False
        if beautiful:
            print(0)
            continue
        
        # Compute x transitions
        x_possible = True
        allowed_x = []
        for i in range(n-1):
            transitions = []
            for s_prev in [0, 1]:
                for s_curr in [0, 1]:
                    valid = True
                    for j in range(n):
                        if h[i][j] + s_prev == h[i+1][j] + s_curr:
                            valid = False
                            break
                    if valid:
                        transitions.append((s_prev, s_curr))
            allowed_x.append(transitions)
            if not transitions:
                x_possible = False
                break
        
        min_x = float('inf')
        if x_possible:
            dp_prev = [0, a[0]]
            for i in range(1, n):
                dp_current = [float('inf'), float('inf')]
                for s_prev, s_curr in allowed_x[i-1]:
                    if dp_prev[s_prev] == float('inf'):
                        continue
                    cost = dp_prev[s_prev] + a[i] * s_curr
                    if cost < dp_current[s_curr]:
                        dp_current[s_curr] = cost
                if dp_current[0] == float('inf') and dp_current[1] == float('inf'):
                    x_possible = False
                    break
                dp_prev = dp_current.copy()
            if x_possible:
                min_x = min(dp_prev)
        
        # Compute y transitions
        y_possible = True
        allowed_y = []
        for j in range(n-1):
            transitions = []
            for s_prev in [0, 1]:
                for s_curr in [0, 1]:
                    valid = True
                    for i in range(n):
                        if h[i][j] + s_prev == h[i][j+1] + s_curr:
                            valid = False
                            break
                    if valid:
                        transitions.append((s_prev, s_curr))
            allowed_y.append(transitions)
            if not transitions:
                y_possible = False
                break
        
        min_y = float('inf')
        if y_possible:
            dp_prev = [0, b[0]]
            for j in range(1, n):
                dp_current = [float('inf'), float('inf')]
                for s_prev, s_curr in allowed_y[j-1]:
                    if dp_prev[s_prev] == float('inf'):
                        continue
                    cost = dp_prev[s_prev] + b[j] * s_curr
                    if cost < dp_current[s_curr]:
                        dp_current[s_curr] = cost
                if dp_current[0] == float('inf') and dp_current[1] == float('inf'):
                    y_possible = False
                    break
                dp_prev = dp_current.copy()
            if y_possible:
                min_y = min(dp_prev)
        
        if x_possible and y_possible:
            print(min_x + min_y)
        else:
            print(-1)

solve()