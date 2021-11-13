
def days_in_month(monthNumber):
    for i in range(1,13):
        if monthNumber == 1:
            print("31")
        elif monthNumber == 2:
            print("28")
        elif monthNumber == 3:
            print("31")
        elif monthNumber == 4:
            print("30")
        elif monthNumber == 5:
            print("31")
        elif monthNumber == 6:
            print("30")
        elif monthNumber == 7:
            print("31")
        elif monthNumber == 8:
            print("31")
        elif monthNumber == 9:
            print("30")
        elif monthNumber == 10:
            print("31")
        elif monthNumber == 11:
            print("30")
        elif monthNumber == 12:
            print("31")
        else:
            print("error")

days_in_month(6)