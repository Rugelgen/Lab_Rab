# TODO Напишите функцию для поиска индекса товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
nujny_towar = ['банан', 'груша', 'персик']
def nah (spis, find_item):
    for i in find_item:
        if i in spis:
                nomer_towara = spis.index(i)
                print(f"Первое вхождение товара '{i}' имеет индекс {nomer_towara}.")
        else:
            print(f"Товар '{i}' не найден в списке.")
nah(items_list,nujny_towar)
