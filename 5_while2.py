"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Любишь отдыхать?': 'Нет, люблю работать!'
}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        answers_dict = input('Пользователь: ').capitalize()
        for questions in questions_and_answers:
            if answers_dict == questions:
                print(f'Программа: {questions_and_answers[answers_dict]}')
        if answers_dict == 'Пока':
            print('Программа: И тебе пока!')
            break


if __name__ == "__main__":
    ask_user(questions_and_answers)
