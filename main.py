cook_book = {}

with open('date.txt') as file:
    for line in file:
        ingridients = []
        name = line.replace('\n', '')
        emp_count = file.readline()
        for i in range(int(emp_count)):
            emp = file.readline().replace('\n','')
            ing, mass, wtf = emp.split(' | ')
            lst = {}
            lst['ingredient_name'] = ing
            lst['quantity'] = mass
            lst['measure'] = wtf
            ingridients.append(lst)
        cook_book[name] = ingridients
        file.readline()
print(cook_book)