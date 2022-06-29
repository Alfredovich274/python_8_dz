print('Привет!')
year = 0
date = [0, '']
while year != 1799:
    year = int(input('В каком году родился А.С.Пушкин? '))
while date[0] != '6' and date[1].lower() != 'июня':
    date = input('Напишите день рождения А.С.Пушкина (пример - "1 мая") ')
    date = date.split()
print('Верно')
