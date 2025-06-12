t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    result = ""
    for char in s:
        if char not in result:
            result += char
    print((len(result) * 2 + (n - len(result))))
        
   
        



