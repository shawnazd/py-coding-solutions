n = int(input())
s = input()

Anton = 0
Danik = 0

for i in range(n):
    if(s[i] == "A"):
        Anton += 1
    elif(s[i] == "D"):
        Danik += 1

if(Anton > Danik):
    print("Anton")
elif(Danik > Anton):
    print("Danik")
elif(Anton == Danik):
    print("Friendship")

