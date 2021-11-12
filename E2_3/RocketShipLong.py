def print_cone():   
    print(r"     ^  ")    
    print(r"    /|\ ")  
    print(r"   //|\\ ") 
    print(r"  ///|\\\  ")

print_cone()

def print_body():
    print(r" +-------+")
    for i in range(4):
        print("+*********+")

for i in range(4):
    print_body()

print(" +-------+")

print_cone()
