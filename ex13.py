sum = 0
x = int(input())
for i in range(x):
    y = int(input())
    sum = sum + y
print("Suma a celor " + str(x) + " numere este: " + str(sum))
print("Media sumei este: " + str(int(sum / x)))
