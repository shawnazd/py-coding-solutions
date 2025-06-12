t = int(input())
for _ in range(t):
    s = input()
    h = len(s) // 2
    if(len(s) % 2 != 0):
        print("NO")
    else:
        if(s[h:] == s[:h]):
            print("YES")
        else:
            print("NO")

