from pprint import pprint

with open('text.txt') as f:
    cook_book = {}
    for line in f:
        name = line.strip()
        ingridients = []
        quantity = int(f.readline().strip())
        components = [f.readline().strip().split(" | ") for i in range(quantity)]
        for lines in components:
            ingridient_dict = {'ingredient_name': lines[0], 'quantity': int(lines[1]), 'measure': lines[2]}
            ingridients.append(ingridient_dict)
        cook_book[name] = ingridients
        f.readline().strip()
pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    spisok = {}
    for dish in dishes:
        if dish in cook_book:
            for name_ in cook_book[dish]:
                name_['quantity'] *= person_count
                if name_['ingredient_name'] not in spisok:
                    spisok[name_['ingredient_name']] = {'measure': name_['measure'], 'quantity': int(name_['quantity'])}
                else:
                    spisok[name_['ingredient_name']]['quantity'] += int(name_['quantity'])
        else:
            print(f'Рецепта для блюда {dish} нет в книге')
    pprint(spisok)


get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Баклажаны', 'Торт'], 5)
