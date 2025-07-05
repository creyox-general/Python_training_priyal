'''
8) input 3 name and related birthdate and find out who is yonger and older.


input

Sagar 31-1-1996

Kishan 30-1-1996

Nikhil 22-7-1989

Output
Kishan is yonger
Nikhil is older

'''

name1 = input("name =")
date1 = int(input("date ="))
month1 = int(input("month ="))
year1 = int(input("year ="))

name2 = input("name =")
date2 = int(input("date ="))
month2 = int(input("month ="))
year2 = int(input("year ="))

name3 = input("name =")
date3 = int(input("date ="))
month3 = int(input("month ="))
year3 = int(input("year ="))

x = min(year1,year2,year3)

x1 = max(year1,year2,year3)
year = {}
year[name1] = year1
year[name2] = year2
year[name3] = year3

#---------------------------------------------------------------------------------------------------

minyear = []
for i in year:
    a = year.get(i)
    if a == x:
        minyear.append(i)

if len(minyear) > 1:
    if len(minyear) == 3:
        if minyear[0]==name1 and minyear[1]==name2 and minyear[2]==name3:
            y = min(month1,month2,month3)
    else:
        if minyear[0]==name1 and minyear[1]==name2:
            y = min(month1,month2)
        elif minyear[0]==name2 and minyear[1]==name3:
            y = min(month2,month3)
        else:
            y = min(month1,month2)

    month = {}
    month[name1] = month1
    month[name2] = month2
    month[name3] = month3

    minmonth = []
    for j in month:
        b = month.get(j)
        if b == y:
            minmonth.append(j)

    if len(minmonth) > 1:

        if len(minmonth) == 3:
            if minmonth[0] == name1 and minmonth[1] == name2 and minmonth[2] == name3:
                z = min(date1, date2, date3)
        else:
            if minmonth[0] == name1 and minmonth[1] == name2:
                z = min(date1, date2)
            elif minmonth[0] == name2 and minmonth[1] == name3:
                z = min(date2, date3)
            else:
                z = min(date1, date2)

        date = {}
        date[name1] = date1
        date[name2] = date2
        date[name3] = date3

        mindate = []
        for k in date:
            c = date.get(k)
            if c == z:
                mindate.append(k)
                print(c)
                print(mindate)

        print(mindate[0], "is older")

    else:
        print(minmonth[0], "is older")

else:
    print(minyear[0], "is older")

#------------------------------------------------------------------------------------------

maxyear = []
for i2 in year:
    a2 = year.get(i2)
    if a2 == x1:
        maxyear.append(i2)

if len(maxyear) > 1:
    if len(maxyear) == 3:
        if maxyear[0]==name1 and maxyear[1]==name2 and maxyear[2]==name3:
            y2 = max(month1,month2,month3)
    else:
        if maxyear[0]==name1 and maxyear[1]==name2:
            y2 = max(month1,month2)
        elif maxyear[0]==name2 and maxyear[1]==name3:
            y2 = max(month2,month3)
        else:
            y2 = max(month1,month2)

    month = {}
    month[name1] = month1
    month[name2] = month2
    month[name3] = month3

    maxmonth = []
    for j2 in month:
        b2 = month.get(j2)
        if b2 == y2:
            maxmonth.append(j2)

    if len(maxmonth) > 1:

        if len(maxmonth) == 3:
            if maxmonth[0] == name1 and maxmonth[1] == name2 and maxmonth[2] == name3:
                z2 = max(date1, date2, date3)
        else:
            if maxmonth[0] == name1 and maxmonth[1] == name2:
                z2 = max(date1, date2)
            elif maxmonth[0] == name2 and maxmonth[1] == name3:
                z2 = max(date2, date3)
            else:
                z2 = max(date1, date2)

        date = {}
        date[name1] = date1
        date[name2] = date2
        date[name3] = date3

        maxdate = []
        for k2 in date:
            c2 = date.get(k2)
            if c2 == z2:
                maxdate.append(k2)


        print(maxdate[0], "is yonger")

    else:
        print(maxmonth[0], "is yonger")

else:
    print(maxyear[0], "is yonger")














