string1 = "12345"
string2 = "abcde"
final_string = ''

all_letters = zip(list(string1)[::-1], list(string2))

for letter1, letter2 in all_letters:
    final_string = final_string + letter1 + letter2

print(final_string)