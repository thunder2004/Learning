def currency_rates(cur_name):
    import requests
    import datetime
    Valute = {}

    cbr_req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    xml_str_data = cbr_req.text
    v_code = ''
    v_data = ''
    current_date = ''

# Убираем все лишнее для преобразования строки в список
    xml_str_data = xml_str_data.replace('</','  ')
    xml_str_data = xml_str_data.replace('<','  ')
    xml_str_data = xml_str_data.replace('>','  ')
    xml_str_data = xml_str_data.replace('    ','  ')
    xml_str_data_list = xml_str_data.split('  ')

    # Заполняем словарь нужными элементами
    for ndx in xml_str_data_list:
        try:
            xml_str_data_list.remove('')
        except:
            break
    for ndx, data1 in enumerate(xml_str_data_list):
        try:
            if data1 == xml_str_data_list[ndx + 2]:
                xml_str_data_list.pop(ndx + 2)
        except:
            break
    for ndx, data1 in enumerate(xml_str_data_list):
        try:
            if data1 == 'CharCode':
                v_code = xml_str_data_list[ndx + 1]
            elif data1 == 'Value':
                Valute.update({v_code : xml_str_data_list[ndx + 1]})
        except:
            break
# Ищем и собираем данные о дате
    for ndx, data1 in enumerate(xml_str_data_list):
        if data1 >= 'ValCurs Date':
            current_date = datetime.date(int(xml_str_data_list[1][20:24]), int(xml_str_data_list[1][17:19]), int(xml_str_data_list[1][14:16]))

    return Valute.get(cur_name), current_date

if __name__ == '__main__':
    import sys

#    val = input('Enter youre currency code: ')
    result = currency_rates(sys.argv[1])
    print('Текущий курс: ', result[0], 'На дату:', result[1])