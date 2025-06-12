t = int(input())
for _ in range(t):
    x = input()
    d = int(x[0])
    l = len(x)

    result = (d - 1) * 10 + ((l * ( l + 1 )) // 2)
    print(result)
