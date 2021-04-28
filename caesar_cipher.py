alpha = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
alphaUp = alpha.upper()

number = int(input('Input a number: '))
summ = ''

def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open('filename.txt', encoding='utf-8') as myFile:
    for line in myFile:
        for char in line:
            summ += changeChar(char)

with open('output.txt', 'w', encoding='utf-8') as myFile:
    myFile.write(summ)
