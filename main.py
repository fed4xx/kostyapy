streight = input('Введите строку: ')
text = list(streight)
normal_text = ''

index = 0
count = 0
for sym in text:
    index += 1
    if sym == ':':
        count += 1
        text[index-1] = ';'
for i in text:
    normal_text += i
print('Исправленная строка:', normal_text)
print('Количество замен:', count)