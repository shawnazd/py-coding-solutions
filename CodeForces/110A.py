n = input()
lucky_count = 0

for num in n:
    if num == "4" or num == "7":
        lucky_count += 1

lucky_count = str(lucky_count)
result = False

for num in lucky_count:
    if num != "4" and num != "7":
        result = False
        break
    else:
        result = True

if result == True:
    print("YES")
else:
    print("NO")

