def print_left_triangle(n):
    for i in range(n):
        print("%"*i)
        for j in range(i+1):
            print("*"*j)


print_left_triangle(4)
