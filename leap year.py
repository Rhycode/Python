year=int(input('Enter year: '))
if (year % 4) == 0:
    
    print('it is a leap year')

    if(year % 100) == 0:
        print('It is a current year')
else:
    print('It is not a leap year')