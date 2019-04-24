year = int(input("연도를 입력하시오: "))
month = int(input("월을 입력하시오: "))

result = 0
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        result = 29
    else :
        result = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    result = 30
elif month == 1 or month == 3 or month == 5 or month == 7 or\
     month == 8 or month == 10 or month == 11:
    result = 31
else :
    result = -1

if result != -1:
    print("월의 날수는 %d입니다." % result)
else :
    print("월은 1~12 사이의 수를 입력하세요.")