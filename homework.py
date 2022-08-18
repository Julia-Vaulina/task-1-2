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
    for dishes in cook_book.items():
         for inn in dishes[1]:
             inn['quantity'] *= person_count
    print(dishes[1])

get_shop_list_by_dishes(['Фахитос'], 2)






