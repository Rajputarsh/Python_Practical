import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation (a cannot be 0).")
else:
    d = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    if d > 0:
        print("Real and distinct roots:", root1.real, root2.real)
    elif d == 0:
        print("Real and equal roots:", root1.real)
    else:
        print("Complex roots:", root1, root2)
