words_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for single_word in words_list:
    try:
        single_word_try = single_word
        int(single_word_try)
        if 1 < len(single_word) < 3 and (str(single_word[0]) == '+' or str(single_word[0]) == '-'):
            single_word = '"' + single_word[0] + '0' + single_word[1] + '"'
            print(single_word, end=' ')
        elif len(single_word) > 1:
            single_word = '"' + single_word + '"'
            print(single_word, end=' ')
        else:
            single_word = '"' + str('0') + single_word + '"'
            print(single_word, end=' ')

    except:
        print(single_word, end=' ')