name = input().strip()

distinct = len(set(name))

if distinct % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
