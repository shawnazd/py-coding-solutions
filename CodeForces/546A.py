k, n, w = map(int, input().split())
banana_price = 0
for i in range(1, w + 1):
    banana_price += (i * k)
if banana_price > n:
    print(banana_price - n)
else:
    print(0) 

