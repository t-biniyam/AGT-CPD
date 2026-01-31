s = input().strip()

upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())

if upper > lower:
    print(s.upper())
else:
    print(s.lower())
