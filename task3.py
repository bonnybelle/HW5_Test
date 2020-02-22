# 3. Есть список объектов. Нужно посчитать сколько раз какой тип данных встречается в списке.
# И вывести только объекты самого частого типа.
from collections import Counter

lst = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1, 2], {1: 1}]
cnt = Counter()
types = [type(j) for j in lst if type(j)]
common_one = Counter(types).most_common(1)
final = [i for i in lst if type(i) == common_one[0][0]]
print('Самый частый тип и количество:', common_one[0], '\nОбъекты этого типа:', final)
