n, h = map(int, input().split())
heights = list(map(int, input().split()))

width = 0
for a in heights:
    if a > h:
        width += 2
    else:
        width += 1

print(width)
