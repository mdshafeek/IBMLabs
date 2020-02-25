def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


x1 = int(input("Enter a number: "))
y1 = int(input("Enter a number: "))
print("The L.C.M of", x1, "and", y1, "is", compute_lcm(x1, y1))
