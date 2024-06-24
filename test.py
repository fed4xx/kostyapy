s = input('Введите строку: ')
position = int(input('Номер символа: '))
s_list = list(s)
symbol = s_list[position-1]
right = s_list[position]
left = s_list[position - 2]
count = -1
for i in s_list:
	if i == symbol:
		count += 1



print('Символ слева:', left, '\nСимвола справа:', right)
print('Таких же символов: ', count)
