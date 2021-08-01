def calc_d(x):
    summ1_all = 0
    for num1 in x:
        temp_summ = 0
        while True:
            temp_summ = temp_summ + (num1 % 10)
            next_d = num1 // 10
            if next_d == 0:
                break
            else:
                num1 = next_d
        if (temp_summ % 7) == 0:
            summ1_all = summ1_all + temp_summ

    return summ1_all


iter1 = 1
coub = list()

while iter1 < 1000:
    coub.append(iter1 ** 3)
    iter1 = iter1 + 2

print("Sum: ", calc_d(coub))

counter1 = 0
for iter1 in coub:
    coub[counter1] = coub[counter1] + 17

print("Sum + 17: ", calc_d(coub))