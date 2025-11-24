def solve(a):

    if len(str(a)) <=2:
        return "NO"

    if str(a)[0] != "1" or str(a)[1] != "0":
        return "NO"
    number_str = str(a)[2:]
    #print(number_str)

    for i in range(0,len(number_str)-1):
        if number_str[i] == "0":
            return "NO"

    if (int(number_str)) >=2:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    a = int(input())
    print(solve(a))
