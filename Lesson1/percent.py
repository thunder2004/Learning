while True:
    num1 = int(input("Enter you're percent:"))
    if num1 == 0:
        break
    else:
         if num1 < 10:
            if (num1 % 10) == 1:
                print(num1, " Процент")
            elif 1 < (num1 % 10) < 5:
                print(num1, " Процента")
            else:
                print(num1, " Процентов")
         else:
             print(num1, " Процентов")