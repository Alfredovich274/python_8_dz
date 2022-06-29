print('Привет!')
year = int(input('В каком году родился А.С.Пушкин? '))
if year == 1799:
    date = input('Напишите день рождения А.С.Пушкина (пример - "1 мая") ')
    date = date.split()
    if date[0] == '6' and date[1].lower() == 'июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
