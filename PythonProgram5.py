'''
5) Enter three input dates with time. Check whether
 third input date is between first and second entered date.

'''

date1 = int(input("date = "))
month1 = int(input("month = "))
year1 = int(input("year = "))
hour1 = int(input("hour = "))
minute1 = int(input("minute = "))
second1 = int(input("second = "))

if  month1 > 12 or date1 > 31 or hour1 > 23 or minute1 > 59 or second1 > 59:
    if month1 == 2 or 4 or 6 or 9 or 11:
        if date1 > 30:
            print("invalid")
            if month1 == 2 and date1 > 29:
                print("invalid")
    print("invalid")

date2 = int(input("date = "))
month2 = int(input("month = "))
year2 = int(input("year = "))
hour2 = int(input("hour = "))
minute2 = int(input("minute = "))
second2 = int(input("second = "))

if  month2 > 12 or date2 > 31 or hour2 > 23 or minute2 > 59 or second2 > 59:
    if month2 == 2 or 4 or 6 or 9 or 11:
        if date2 > 30:
            print("invalid")
            if month2 == 2 and date2 > 29:
                print("invalid")
    print("invalid")

date3 = int(input("date = "))
month3 = int(input("month = "))
year3 = int(input("year = "))
hour3 = int(input("hour = "))
minute3 = int(input("minute = "))
second3 = int(input("second = "))

if  month3 > 12 or date3 > 31 or hour3 > 23 or minute3 > 59 or second3 > 59:
    if month3 == 2 or 4 or 6 or 9 or 11:
        if date3 > 30:
            print("invalid")
            if month3 == 2 and date3 > 29:
                print("invalid")
    print("invalid")

if year1 <= year3 and year3 <= year2:
   if month1 <= month3 and month3 <= month2:
       if date1 < date3 and date3 < date2:
           print("Yes")
       else:
           print("No")
   else:
       print("No")
else:
    print("No")