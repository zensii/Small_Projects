import random
end_game = False
total_tasks = 0
total_correct = 0
total_wrong = 0
total_wrong_tries = 0
add = ''

print('Здравей, кой ще играе днес? ')
print('1: 👦')
print('2: 👧')

while True:
    try:
        sex = int(input('Избери играч: '))
        if sex in (1, 2):
            break
        else:
            print('Трябва да избереш играч "1" или играч "2"')
    except ValueError:
        print('Избери си играч и напиши "1" или "2"')

user = input('Как се казваш?: ')
if sex == 2:
    add = 'a'
print()
print(f'Здравей {user.capitalize()}. Нека проверим дали си научил{add} таблицата за умножение и деление. ')
print('Когато искаш да спреш просто въведи "стоп".')
print()
print('Каво искаш да тренираш този път?')
print('1: Умножение. ')
print('2: Деление.')
print('3: и двете.')

while True:
    try:
        type_of_game = int(input('Избирам... '))
        if type_of_game in (1, 2, 3):
            break
        else:
            print('Трябва да избереш какво искаш да тренираш и да въведеш "1","2" или "3"')
    except ValueError:
        print('Избери и напиши "1","2" или "3"')

if type_of_game == 3:
    print(f'Ооо, чувстваш се смел{add} днес а?')

start = input('Натисни "Enter" за да стартираш играта.')

while not end_game:

    next_question = False
    answer = 0
    tries = 0
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    divisors = [a, b]
    if type_of_game == 3:
        operations = ['multiplication', 'division']
        operation = random.choice(operations)
    elif type_of_game == 2:
        operation = 'division'
    elif type_of_game == 1:
        operation = 'multiplication'

    divided = a * b
    divisor = random.choice(divisors)

    if operation == 'division':

        correct = divided // divisor
        print()
        print('--------------------------------------')
        print()
        print(f'Колко е {divided} ÷ {divisor} ?')
    else:
        correct = a * b
        print()
        print('--------------------------------------')
        print()
        print(f'Колко е {a} * {b} ?')

    while not end_game:
        while tries != 2:
            user_input = input('Чакам отговора ти: ').lower()

            if user_input in ('stop', 'стоп'):
                end_game = True
                print()
                print('**************************************')
                print()
                print(f'Отлича работа {user.capitalize()}!. Ти реши {total_tasks} задачи.')
                print(f'От тях реши вярно {total_correct}, като ти бяха необходими {total_wrong_tries + total_correct} опита.')
                print(f'Имаше и {total_wrong} грешки.')
                break
            else:
                try:
                    answer = int(user_input)
                    break
                except ValueError:
                    print('Моля, въведи цяло число или напиши "стоп" за да спреш играта.')

        if not end_game:
            tries += 1
            if answer == correct:
                print()
                print('😄')
                print(f'Правилен отговор. Браво! {user.capitalize()}!')
                total_correct += 1
                total_tasks += 1
                break
            elif tries == 1:
                print()
                print('Грешен отговор. Имаш само  един шанс: ')
                total_wrong_tries += 1
            elif tries == 2:
                print()
                print('😵')
                print('Не позна!')
                print(f'Верният отговор е: {divided} ÷ {divisor} = {correct}')

                total_tasks += 1
                total_wrong += 1

                break

print()
exit_program = input("Натисни 'Enter' за да затвориш програмата")