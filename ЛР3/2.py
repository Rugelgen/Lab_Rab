# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
znak_razdel = '|'
def find_common_participants(first_gr, second_gr, razdel_=","):
    first_gr = first_gr.split(razdel_)
    second_gr = second_gr.split(razdel_)
    first_gr = set(first_gr)
    obchie_uch_set = first_gr.intersection(second_gr)
    obchie_uch_str = ', '.join([str(item) for item in obchie_uch_set]) # перевод в строку
    obchie_uch_list = obchie_uch_str.split(', ')# перевод в список
    return obchie_uch_list

print(find_common_participants(participants_first_group,participants_second_group,znak_razdel))
print(type(find_common_participants(participants_first_group,participants_second_group,znak_razdel)))
# TODO Провеьте работу функции с разделителем отличным от запятой
