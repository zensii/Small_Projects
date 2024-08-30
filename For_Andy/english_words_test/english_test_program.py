import random
add = ''
target_word = None
end_game = False
random_word = None
random_choice = None
next_word = False
total_translations = 0
total_errors = 0
wrong_words = []

print('Здравей, кой ще играе днес? ')
print('1: 👦')
print('2: 👧')
print('Избери "1" или "2"')
while True:
    try:
        sex = int(input('Избери играч:'))
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
print(f'Здравей {user.capitalize()}. Нека проверим дали си знаеш думите по Английски.')
print()
print('Каво искаш да упражняваш този път?')
print()
print('1: превод от Английски към Български,')
print('2: превод от Български към Английски')
print('3: или и двата вида?')
print()

while True:
    try:
        type_of_game = int(input('Избирам...'))
        if type_of_game in (1, 2, 3):
            break
        else:
            print('Трябва да избереш какво искаш да тренираш и да въведеш "1","2" или "3"')
    except ValueError:
        print('Избери и напиши "1","2" или "3"')

if type_of_game == 3:
    print()
    print(f'Ооо, чувстваш се смел{add} днес а?')

print('Успех! Когато искаш да спреш просто въведи "стоп".')
print()
start = input('Натисни "Enter" за да стартираш играта.')


#  ///////////////////////////////////////////////////////////////////////////////////////  # user selection
words_dict = {}

with open('dictionary.txt', 'r', encoding='utf-8') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into key and value using the colon as delimiter
        key, value = line.strip().split(',')
        # Add the key-value pair to the dictionary
        words_dict[key.strip()] = value.strip()

while not end_game:

    random_en_word = random.choice(list(words_dict.keys()))  # select random english word from dictionary
    random_bg_word = random.choice(list(words_dict.values()))  # select random bulgarian word from dictionary

    if type_of_game == 1:
        random_word = random_en_word
        translation = 'Български'
    elif type_of_game == 2:
        random_word = random_bg_word
        translation = 'Английски'
    else:

        random_choices = [1, 2]
        random_choice = random.choice(random_choices)
        if random_choice == 1:
            random_word = random_en_word
            translation = 'Български'
        else:
            random_word = random_bg_word
            translation = 'Английски'
    print()
    print('-------------------------------------------------------')
    print()
    print(f'как се превежда "{random_word}" на {translation}?')

    if type_of_game == 2 or (type_of_game == 3 and random_choice == 2):
        for key, item in words_dict.items():
            if item == random_word:
                target_word = key

    elif type_of_game == 1 or (type_of_game == 3 and random_choice == 1):
        target_word = words_dict[random_en_word]
    tries = 0
    while True:

        if tries < 2:
            user_input = input('Очаквам отговора ти:')
            if user_input == 'stop' or user_input == 'стоп':
                print()
                print('#############################################################')
                print(f'{user.capitalize()} ти преведе {total_translations} думи.')
                print(f'Имаше и {total_errors} грешки.')
                print(f'Думите, с които се затрудни бяха: {wrong_words}')

                end_game = True
                break
            else:
                guess = user_input

            if guess == target_word:
                print('Правилно! 😊👍')
                total_translations += 1
                next_word = True
                break
            else:
                tries += 1
                print()
                print('Грешка!')
                print('Помисли и опитай още веднъж.')
        else:
            print()
            print('******')
            print(f'Не успя да се сетиш {user.capitalize()} 😵')
            print(f'Преводът на "{random_word.upper()}" e "{target_word.upper()}"')
            total_errors += 1
            wrong_words.append(random_word)
            break
print()
print('Успех с ученето на английския език!')
print()
program_stop = input('Натисни "Enter за да затвориш програмата"')