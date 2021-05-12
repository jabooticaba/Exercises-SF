def ranging2(x):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
            if x[j] == x[j+1]:
                x.pop(j)
    return x


def search_binary(list, targ, left_half, right_half):
    """Поиск элемента target в списке list"""
    if left_half > right_half:
        return False

    middle = left_half + (right_half - left_half) // 2
    if list[middle] == targ:
        if list[0] == targ:
            return f'введённое число - наименьшее в списке, его индекс: 0'
        if list[-1] == targ:
            return f'{middle - 1}, введённое число - наибольшее в списке'
        else:
            return middle-1, middle

    elif targ < list[middle]:
        return search_binary(list, targ, left_half, middle - 1)
    else:
        return search_binary(list, targ, middle + 1, right_half)

    
try:
    raw_input = '1 2 3 5 6 7'
    target = int(input())
    format_list = list(map(int, raw_input.split())) + [target]  # Преобразование в список, добавление введённого числа
except Exception as e:
    print("Введённые числа не соответствуют параметрам задания")

else:
    print(search_binary(ranging2(format_list), target, 0, len(format_list)))
