t = int(input())  # Number of test cases
correct = "Timur"

for _ in range(t):
    n = int(input())
    s = input()
    
    if n == 5 and sorted(s) == sorted(correct):
        print("YES")
    else:
        print("NO")


