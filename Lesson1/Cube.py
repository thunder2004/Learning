i = 1
coub = list()
summ_of_char = list()
while i < 1000:
    x = i ** 3
    coub.append(x)
    i = i + 2
#print(coub)
for j in coub:
    ch_summ = 0
    for character in str(j):
        ch_summ = ch_summ + int(character)
    if (ch_summ % 7) == 0:
        summ_of_char.append(int(ch_summ))

print(summ_of_char)

x = 0
for i in coub:
    coub[x] += 17

for j in coub:
    ch_summ = 0
    for character in str(j):
        ch_summ = ch_summ + int(character)
    if (ch_summ % 7) == 0:
        print(ch_summ, end=", ")