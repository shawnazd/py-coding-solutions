s = input()
upper_count = 0
lower_count = 0
for char in s:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
if lower_count >= upper_count:
    print(s.lower())
else:
    print(s.upper())