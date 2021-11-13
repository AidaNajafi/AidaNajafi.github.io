
monthNumber = int(input("Enter monthnumber:"))
def print_month(monthNumber):
    for i in range(1,13):
        if monthNumber == 1:
            print("January")
        elif monthNumber == 2:
            print("Febuary")
        elif monthNumber == 3:
            print("March")
        elif monthNumber == 4:
            print("April")
        elif monthNumber == 5:
            print("May")
        elif monthNumber == 6:
            print("June")
        elif monthNumber == 7:
            print("July")
        elif monthNumber == 8:
            print("August")
        elif monthNumber == 9:
            print("September")
        elif monthNumber == 10:
            print("October")
        elif monthNumber == 11:
            print("November")
        elif monthNumber == 12:
            print("December")
        else:
            print("error")

print_month(1)
print_month(2)
print_month(3)
print_month(4)
print_month(5)
print_month(6)
print_month(7)
print_month(8)
print_month(9)
print_month(10)
print_month(11)
print_month(12)