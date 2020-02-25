year = int(input("Enter a Year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if(year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is a not leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is a not leap year".format(year))
