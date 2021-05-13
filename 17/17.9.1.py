def ranging(x):
    """Сортировка вставками"""
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


def search_binary(list, targ, left_half, right_half):
    """Поиск элемента target в списке list"""
    if left_half > right_half:
        return False

    middle = left_half + (right_half - left_half) // 2
    if list[middle] == targ:
        if list[0] == targ:
            return f'Введённое число - наименьшее в списке'
        if list[-1] == targ:
            return f'Введённое число - наибольшее в списке'
        else:
            x = 1
            while list[middle] == list[middle-x]:
                x += 1
            return f'Позиция предыдущего элемента в списке: {middle-x+1}'  # f'Позиция следующего элемента в списке: {middle-x+2}'

    elif targ < list[middle]:
        return search_binary(list, targ, left_half, middle - 1)
    else:
        return search_binary(list, targ, middle + 1, right_half)

    
def input_val():
    while type:
        raw_string = input("Введите целые числа через пробел: ")
        try:
            base_list = list(map(int, raw_string.split()))
            if len(base_list) == 0:
                raise ValueError
        except ValueError:
            print("Неверный формат данных")
        else:
            break
            
    while True:
        digit = input("Введите целое число: ")
        try:
            target = int(digit)
        except ValueError:
            print('"{0}" не является целым числом'.format (digit))
        else:
            break
    formatted_list = base_list + [target]    
    print(search_binary(ranging(formatted_list), target, 0, len(formatted_list)))

input_val()
