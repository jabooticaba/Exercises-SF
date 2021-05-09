# Вставка элемента в конец массива, измерение разницы времени обработки между массивами с двухкратной разницей элементов (100 ранов) - сложность О(т)

import timeit

def elapsed_time(func, size):
  ''' Функция принимает данные в виде строки (string), потому код блока code_append закомментирован. 
  % size позволяет подставлять данные в эту строку (%d) - количество элементов внутри списка elements'''
  return timeit.timeit(func % size, number=100)/100


code_append = """
elements = range(%d) # генератор элементов, которые будут вставляться в список
array = [] # список, работу которого тестируем
for e in elements:
    array.append(e) # добавляем каждый раз в конец
"""


for s in range(10,15):
    measure_1 = elapsed_time(code_append, 2**s) # 2**s - 2 в степени 10-15, количество элементов списка, подставляем в функцию elapsed_time как 
    measure_2 = elapsed_time(code_append, 2**(s+1)) # параметр size и, таким образом, в генератор списка elements = range(%d)
    ratio = measure_2 / measure_1
    print("[%d]/[%d] -> %5.2f" % (2**(s+1), 2**s, ratio))
    
    
    
# То же, но вставка элемента в начало списка 
    
    import timeit

def elapsed_time(func, size):
    return timeit.timeit(func % size, number=100)/100


code_insert = """
elements = range(%d) # генератор элементов, которые будут вставляться в список
array = [] # список, работу которого тестируем
for e in elements:
    array.insert(0, e) # добавляем каждый раз в начало
"""


for s in range(10,12):
    measure_1 = elapsed_time(code_insert, 2**s)
    measure_2 = elapsed_time(code_insert, 2**(s+1))
    ratio = measure_2 / measure_1
    print("[%d]/[%d] -> %5.2f" % (2**(s+1), 2**s, ratio))
