s = input()
t = input()

reversed_s = "".join(reversed(s))

if(reversed_s == t):
    print("YES")
else:
    print("NO")