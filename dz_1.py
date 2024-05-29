from pprint import pprint

# Задача №1
cook_book = {}
with open("recipes.txt",encoding="utf-8") as f:
    dishes = ""
    for line in f:
        line = line.strip()
        if line.isdigit():
             continue
        elif line and "|" not in line:
            cook_book[line] = []
            dishes = line
        elif line and "|" in line:
            a, b, c = line.split("|")
            cook_book.get(dishes).append(dict(ingredient_name=a, quantity=int(b), measure=c))

pprint(cook_book)

#Задача №2
def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] in shop_list:
                    shop_list[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"] * person_count
                else:
                    shop_list[ingredient["ingredient_name"]] = ({"measure": ingredient["measure"], "quantity":
                                                                (ingredient["quantity"] * person_count)})
        else:
            print("Такого блюда нет в книге")
    return shop_list


pprint(get_shop_list_by_dishes(["Омлет", "Утка по-пекински"], 5))



