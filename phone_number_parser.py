'''
Написать программу декодирования телефонного номера для АОН.
По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
— Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
— Каждая значащая цифра повторяется минимум 2 раза
— Если в номере идут несколько цифр подряд, то для обозначения «такая же цифра как предыдущая» используется идущий 2 или более подряд раз знак #

Например, входящая строка 4434###552222311333661 соответствует номеру 4452136.
Без регулярок!
'''
x = "4434###552222311333661"
post = ""
post2 = ""
number = []
append_flag = False

for char in x:
    if char == post and append_flag == False and char != "#":
        number.append(char)
        append_flag = True
        
    elif char == post and char != number[-1] and char != "#" or post2 == "#":
        number.append(char)
        append_flag = True
        
    elif char == "#" and post == "#" and post2 == "#" and append_flag == True:
        number.append(number[-1])
        append_flag = False
    
    post, post2 = char, post
    
print(number)
