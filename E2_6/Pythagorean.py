for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            if a*a == b*b + c*c:
                print(a , b , c)
            elif b*b == a*a + c*c:
                print(b , a , c)
            elif c*c == a*a + b*b:
                print(c , a , b)