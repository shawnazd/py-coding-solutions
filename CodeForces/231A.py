n = int(input())
x = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if(a[0] + a[1] + a[2]) >= 2:
        x += 1

print(x)