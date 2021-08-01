while True:
    num1 = int(input("Enter you're percent:"))
    if num1 <= 0:
        break
    elif num1 == 1:
        print(num1, " Процент")
    elif 1 < num1 < 5:
        print(num1, " Процента")
    else:
        print(num1, " Процентов")