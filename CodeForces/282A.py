n = int(input())
x = 0
for _ in range(n):
    s = input()
    if "++" in s:
        x += 1
    if "--" in s:
        x -= 1

print(x)
    