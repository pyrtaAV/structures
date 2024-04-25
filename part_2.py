try:
    L = int(input('Введите длину: '))
    M = int(input('Введите массу: '))
    B = int(input('Введите кол-во байт: '))
    X = int(input('Введите отрезок Х: '))
    Y = int(input('Введите отрезок У: '))
    two_number = int(input('Введите двузначное число: '))
    three_number = int(input('Введите трехзначное число: '))
except ValueError as e:
    L = 0
    M = 0
    B = 0
    X = 0
    Y = 0
    two_number = 0
    three_number = 0
    print('Вы ввели неверное значение!')

print(f'1. Количество полных метров: {L // 100}')
print(f'2. Количество полных тонн: {M // 1000}')
print(f'3. Количество полных килобайт: {B // 1024}')

print(f'4. Количество полных отрезков В на отрезке А: {X // Y}')

print(f'5. Количество незанятой части на отрезке А: {X % Y}')

print(f'6. Первая цифра числа: {two_number // 10}, Вторая цифра числа: {two_number % 10}')

print(f'7. Сумма цифр числа: {two_number // 10 + two_number % 10}, '
      f'Произведение цифр числа: {two_number // 10 * two_number % 10}')

new_two_number = str(two_number % 10) + str(two_number // 10)
print(f'8. Новое число: {int(new_two_number)}')

print(f'9. Первая цифра трехзначного числа: {three_number // 100}')

print(f'10. Последняя цифра трехзначного числа: {three_number % 10}, '
      f'Средняя цифра трехзначного числа: {three_number // 10 % 10}')


