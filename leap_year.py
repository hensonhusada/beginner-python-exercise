def is_leap_year(year):
    if year%400 == 0:
        return('Leap Year')

    if year%100 == 0:
        return('Common Year')
    elif year%4 == 0:
        return('Leap Year')
    else:
        return('Common Year')

while True:
    choice = input('Enter year after 1582: ')
    if int(choice) < 1583:
        print('%s is before 1582' %choice)
        continue
    print(is_leap_year(int(choice)))
    