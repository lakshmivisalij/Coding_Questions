is_leap_year = lambda y: y%4==0 and (y%100!=0 or y%400==0)
print(is_leap_year(2008))
