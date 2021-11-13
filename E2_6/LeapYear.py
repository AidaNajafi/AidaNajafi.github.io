def is_leap_year(y):
    if y % 400==0 or y % 4==0 and y % 100!=0 :

        print(True)
    else:
        print(False)

is_leap_year(1792) 
is_leap_year(1796) 
is_leap_year(1800)
is_leap_year(1804) 
is_leap_year(1900)
is_leap_year(1904)
is_leap_year(2000) 
is_leap_year(2004)


