print('Здравствуйте! Как Вас зовут?')
name = input()
print(f'Очень приятно, {name}! Меня зовут Марк.')
print('Сколько Вам лет?')
age = int(input())
my_age = 78
age_difference = my_age - age
if age_difference > my_age:
    print(f'Да, {name}, я старше Вас на {age_difference} лет.')
else:
    print(f'Да, {name}, вы старше меня на {abs(age_difference)} лет.')
print('Вам нравится программировать?')
programming = input()
if programming.lower() == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных '
          'и хороших программ.')
elif programming.lower() == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')