


# def average_of_squares0(n):
#     sum = 0
#     for i in range(1,n-1):
#         sum += i*i
#         result = sum / int(n-2)
#         print(result)
   
# average_of_squares0(5) 

def average_of_squares1(n):
    sum = 0
    for i in range(1,n):
        sum += i*i
        result = sum / int(n-1)
        print(result)
average_of_squares1(4)
# it is the same as average_of_squares0; because the upper limit in average_of_squares0 was 
# n-1 which would result in 5-1 which equals to 4. Also in average_of_squares1, the upper limit was n and the input was 4.