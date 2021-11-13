def compute_sum(n): 
    sum = 0 
    for i in range(1, n+1): 
        sum = sum + i 
    return sum 

 
print("N      compute_sum(N)") 

print("---------------------") 

for i in range(9, 0, -1): 

    print(i, "         ", compute_sum(i)) 