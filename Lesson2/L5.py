from random import uniform
def pr_print(data):
    for i in data:
        print(i.split('.')[0], 'руб.', i.split('.')[1], 'коп.', end=', ')
    print('\n\n')

price_list = list()
for i in range(21):
    price_list.append(str(round(uniform(1, 100), 2)))

print('Price  id:', id(price_list))
pr_print(price_list)

price_list.sort()
print('Price  id after Sort:', id(price_list))
print('Цены отсортированы по возрастанию:')
pr_print(price_list)

price_list_copy = price_list.copy()
price_list_copy.reverse()
print('Цены отсортированы по убыванию:')
pr_print(price_list_copy)

print('Пять самых дорогих товаров:')
pr_print(price_list_copy[0:4])

