# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))

def is_divisible(a, b):
    if a%b==0:
        print(True)
    else:
        print(False)
        return True

def is_prime(n):
    assert n>0 
    assert n < 100
    for n in range(2,100):
        for x in range(2,n):
           if is_divisible(n, x) == False:
               print(n)
is_prime()       
        




