import cmath
a = int(input("Enter a(a!=0):"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

d = (b**2)-(4*a*c)
formula1= (-b + cmath.sqrt(d))/2*a
formula2 = (-b - cmath.sqrt(d))/2*a
if d>0:
    print("the results are {} and {}".format(formula1, formula2))
if d == 0:
    print("the result is{}".format(formula1))
if d < 0:
    print("the results are complex")

