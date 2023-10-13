sum = 0
x = 1
for y in range(0, 21, 1):
    if x % 2 != 0:
        sum = sum + y
    x = x + 2
print(sum)
