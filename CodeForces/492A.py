n = int(input())
total = 0
height = 0

for i in range(1, n + 1):
    blocks = i * (i + 1) // 2 
    total += blocks
    if total > n:
        break
    height += 1

print(height)
