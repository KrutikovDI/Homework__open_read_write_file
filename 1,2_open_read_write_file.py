with open('recipes.txt', 'r') as f:
    cook_book = {}
    for line in f:
        name_dish = line.strip()
        num_dish = int(f.readline())
        composition = []
        for i in range(num_dish):
            ingr_dish = f.readline().strip()
            ingredient_name, quantity, measure = ingr_dish.split(' | ')
            composition.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[name_dish] = composition
import json
print(f'cook_book = {json.dumps(cook_book, indent=1, ensure_ascii=False)}')


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for i in cook_book:
        if i in dishes:
            for k in cook_book[i]:
                dishes_dict[k['ingredient_name']] = {'measure' : k['measure'], 'quantity' : int(k['quantity']) * person_count}
    import json
    print(json.dumps(dishes_dict, separators=(', ', ': '), indent=2, ensure_ascii=False))

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)