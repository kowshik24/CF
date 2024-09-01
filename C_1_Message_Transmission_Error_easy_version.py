def find_original_message(t):
    n = len(t)
    
    # Check all possible lengths of the original message s
    for i in range(1, n):
        s = t[:i]
        if t.startswith(s) and t.endswith(s):
            # Check if the middle part can be formed by merging s with itself
            if t == s + t[i:]:
                continue
            if t[i:-i] == s:
                return "YES\n" + s
    
    return "NO"

# Read input
t = input().strip()

# Find and print the result
print(find_original_message(t))
