import random
def generate_math_question(a, b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(['+', '-', '*', '/'])
    return f'{num1} {operator} {num2}'




def check_answer(question, user_answer):
    try:
        user_answer = float(user_answer)
        if '/' in question:
            return round(user_answer, 1) == eval(question)
        else:

            return user_answer == eval(question)
    except ValueError:
        return False

def math_quiz(number_of_question):
    print('Добро пожаловать в математический тест')
    correct_answer = 0

    for i in range(number_of_question):
        question = generate_math_question(1, 10)
        user_answer = input(f'{question} = ')
        if check_answer(question, user_answer):
            correct_answer += 1
    print('Тест завершен')
    print(f'Вы правильно решили {correct_answer} из {number_of_question}')
math_quiz(5)















