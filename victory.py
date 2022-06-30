import random

people = {'А.С.Пушкина': '1799',
          'Исаака Ньютона': '1643',
          'Христофора Колумба': '1451',
          'Альберта Эйнштейна': '1879',
          'Никола Тесла': '1856',
          'Стива Джобса': '1955',
          'Чарльза Дарвина': '1889',
          'Михаила Ломоносова': '1711',
          'Екатерины 2': '1729',
          'Коко Шанель': '1883'
          }

print('Приветствую тебя на викторине!',
      '\nТебе предстоит отгадать года рождения нескольких известных людей\n')
game = True
while game:
    key_people = list(people.keys())
    names = []
    quantity = random.randint(5, len(key_people) - 1)
    while len(names) < quantity:
        name = random.randint(0, len(key_people) - 1)
        if name not in names:
            names.append(name)

    answers = {}
    right_answers = 0
    for i in names:
        text = 'Напишите пожалуйста год рождения ' + key_people[i] + ' '
        year = input(text)
        answers[key_people[i]] = year
        if answers[key_people[i]] == people[key_people[i]]:
            right_answers += 1

    print('\nKоличество правильных ответов - ', right_answers)
    print('Kоличество ошибок - ', len(names) - right_answers)
    print('Процент правильных ответов - ',
          round(right_answers * 100 / len(names)))
    print('Процент неправильных ответов - ',
          round((len(names) - right_answers) * 100 / len(names)))

    if input('Если желаете начать игру сначала, введите любой символ - ') == '':
        game = False
        print()
