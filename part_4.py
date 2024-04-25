numbers = [1, 2, 3, 4, 5]
city = ['Ростов', '+', 'на', '-', 'Дону']
massive = ['a', 's', '1', 'a', '32', '23']

print(f'Первый элемент списка: {numbers[0]}, Третий элемент спска: {numbers[2]}, Срез списка из первых трех элементов: {numbers[:3]}')

city[1] = '-'
print(f'{city[0]}{city[1]}{city[2]}{city[3]}{city[4]}')

massive_with_numbers = []
massive_with_char = []

for symbols in massive:
    if symbols.isnumeric():
        
        massive_with_numbers.append(int(symbols))
    else:
        massive_with_char.append(symbols)
        
print(f'Массив с числами: {massive_with_numbers}, Массив с буквами: {massive_with_char}')

massive_with_char.pop(-1)
massive_with_char.reverse()
print(massive_with_char)

set_with_symbols = set(massive)
print(massive)
print(set_with_symbols)