# 3. Есть список объектов. Нужно посчитать сколько раз какой тип данных встречается в списке.
# И вывести только объекты самого частого типа.
from collections import Counter

a = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1, 2], {1: 1}]
lst = []
cnt = Counter()
for i in a:
    lst.append(type(i))
print('Объекты самого частого типа:', Counter(lst).most_common(1))
