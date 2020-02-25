def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


x1 = int(input("Enter a number: "))
y1 = int(input("Enter a number: "))
print("The H.C.F of", x1, "and", y1, "is", compute_hcf(x1,y1))