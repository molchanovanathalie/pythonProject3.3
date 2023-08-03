# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
#
#
my_list = [1, 2, 3, 4, 5,'a','b','a', 4, 5]
my_set = set(my_list)
new_list = []

for i in my_set:
     quantity = 0
     for j in my_list:
         if i == j:
             quantity += 1
     if quantity > 1:
         new_list.append(i)
print(new_list)

