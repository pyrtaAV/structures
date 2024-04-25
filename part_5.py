human = {'name': 'Alex', 'age': 34, 'sex': 'male', 'growth': '187', 'weight': 94, }

for key, value in human.items():
    print(f'{key}: {value}')
    
human['shoe size'] = 45
human.pop("age")

print(human)