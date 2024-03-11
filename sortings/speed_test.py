import time
from copy import deepcopy
from functools import wraps
from random import randint

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from count_sort import count_sort
from merge_sort import kmerge_sort, merge_sort
from quick_sort import quick_sort


def time_of(func):
    @wraps(func)  # сохранить метаданные исходной функции
    def inner(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(f'Время выполнения {func.__name__}: {time.time() - t}')
        return res
    return inner


if __name__ == "__main__":
    a = [randint(100000, 1000000000000000) for i in range(100000)]

    print("Большие случайные числа:")
    time_of(insertion_sort)(deepcopy(a))
    time_of(bubble_sort)(deepcopy(a))
    time_of(selection_sort)(deepcopy(a))
    #### time_of(count_sort)(deepcopy(a))  # too long
    time_of(merge_sort)(deepcopy(a))
    time_of(kmerge_sort)(deepcopy(a), 0, len(a) - 1)
    time_of(quick_sort)(deepcopy(a))
    time_of(deepcopy(a).sort)()

    a = [randint(0, 100) for i in range(100000)]

    print("Маленькие случайные числа:")
    time_of(insertion_sort)(deepcopy(a))
    time_of(bubble_sort)(deepcopy(a))
    time_of(selection_sort)(deepcopy(a))
    time_of(count_sort)(deepcopy(a))
    time_of(merge_sort)(deepcopy(a))
    time_of(kmerge_sort)(deepcopy(a), 0, len(a) - 1)
    time_of(quick_sort)(deepcopy(a))
    time_of(deepcopy(a).sort)()

    a = [i for i in range(100000, 0, -1)]

    print("Массив отсортирован по убыванию:")
    time_of(insertion_sort)(deepcopy(a))
    time_of(bubble_sort)(deepcopy(a))
    time_of(selection_sort)(deepcopy(a))
    time_of(count_sort)(deepcopy(a))
    time_of(merge_sort)(deepcopy(a))
    time_of(kmerge_sort)(deepcopy(a), 0, len(a) - 1)
    time_of(quick_sort)(deepcopy(a))
    time_of(deepcopy(a).sort)()

    a = [i for i in range(100000)]

    print("Массив отсортирован по возрастанию:")
    time_of(insertion_sort)(deepcopy(a))
    time_of(bubble_sort)(deepcopy(a))
    time_of(selection_sort)(deepcopy(a))
    time_of(count_sort)(deepcopy(a))
    time_of(merge_sort)(deepcopy(a))
    time_of(kmerge_sort)(deepcopy(a), 0, len(a) - 1)
    time_of(quick_sort)(deepcopy(a))
    time_of(deepcopy(a).sort)()
# Большие случайные числа:
# Время выполнения insertion_sort: 468.4025661945343
# Время выполнения bubble_sort: 958.4248094558716
# Время выполнения selection_sort: 519.6594023704529
# Время выполнения merge_sort: 0.6939973831176758
# Время выполнения kmerge_sort: 0.4220092296600342
# Время выполнения quick_sort: 0.47600221633911133
# Время выполнения sort: 0.03798222541809082
# Маленькие случайные числа:
# Время выполнения insertion_sort: 338.8592941761017
# Время выполнения bubble_sort: 1161.1790475845337
# Время выполнения selection_sort: 522.9940438270569
# Время выполнения count_sort: 0.021981000900268555
# Время выполнения merge_sort: 0.9899861812591553
# Время выполнения kmerge_sort: 0.5909769535064697
# Время выполнения quick_sort: 0.13800501823425293
# Время выполнения sort: 0.016003131866455078
# Массив отсортирован по убыванию:
# Время выполнения insertion_sort: 680.9944036006927
# Время выполнения bubble_sort: 994.5596656799316
# Время выполнения selection_sort: 318.78416299819946
# Время выполнения count_sort: 0.03698444366455078
# Время выполнения merge_sort: 0.4940018653869629
# Время выполнения kmerge_sort: 0.36402320861816406
# Время выполнения quick_sort: 0.23998785018920898
# Время выполнения sort: 0.0010001659393310547
# Массив отсортирован по возрастанию:
# Время выполнения insertion_sort: 0.015000104904174805
# Время выполнения bubble_sort: 420.966427564621
# Время выполнения selection_sort: 309.93124413490295
# Время выполнения count_sort: 0.037036895751953125
# Время выполнения merge_sort: 0.5090045928955078
# Время выполнения kmerge_sort: 0.3890047073364258
# Время выполнения quick_sort: 0.24802041053771973
# Время выполнения sort: 0.0010061264038085938
