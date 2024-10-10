import random

from For_Andy.english_words_test.funcs.funcs import selector, select_player, get_name, get_game_type, add_word, \
    collect_new_english_word, collect_new_bulgarian_word, check_spelling, get_words_dict, record_session, \
    show_dictionary

target_word = None
end_game = False
random_word = None
random_choice = None
next_word = False
total_translations = 0
total_errors = 0
wrong_words = []
words_dict = get_words_dict()

print('Здравей отново, какво ще правим днес?')
while True:
    selection = selector()
    if selection == '1':
        sex, add = select_player()
        user = get_name()
        type_of_game = get_game_type(user, sex)
        break
    elif selection == '2':
        counter = 0
        while True:
            new_english = collect_new_english_word()
            english_check, bulgarian_check = check_spelling(new_english)
            if english_check == 'not_found':
                print("Check english word spelling: ")
                continue
            while True:
                new_bulgarian = collect_new_bulgarian_word()
                if new_bulgarian == bulgarian_check or counter == 1:
                    final_check = input(f"Сигурен ли си, че искаш да добавиш: {english_check}:{new_bulgarian} в речника? ")
                    if final_check.lower() in 'yesдаdaъес1':
                        add_word(new_english, new_bulgarian)
                        break
                    else:
                        continue
                else:
                    print("превода на български е некоректен. Моля провери.")
                    print(f"може би трябва да е: {bulgarian_check}?")
                    counter += 1
                    continue
            break
    elif selection == '3':
        show_dictionary(words_dict)

    else:
        print('Bye bye...!')
        exit()
    print("\nА сега какво ще правим?")

start = input('Натисни "Enter" за да стартираш играта.')

#  ///////////////////////////////////////////////////////////////////////////////////////  # user selection

while not end_game:
    random_en_word = random.choice(list(words_dict.keys()))  # select random english word from dictionary
    random_bg_word = random.choice(list(words_dict.values()))  # select random bulgarian word from dictionary

    if type_of_game == '1':
        random_word = random_en_word
        translation = 'Български'
    elif type_of_game == '2':
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

    print('\n-------------------------------------------------------\n')
    print(f'как се превежда "{random_word}" на {translation}?')

    if type_of_game == '2' or (type_of_game == '3' and random_choice == 2):
        for key, item in words_dict.items():
            if item == random_word:
                target_word = key

    elif type_of_game == '1' or (type_of_game == '3' and random_choice == 1):
        target_word = words_dict[random_en_word]
    tries = 0
    while True:

        if tries < 2:
            user_input = input('Очаквам отговора ти:')
            if user_input == 'stop' or user_input == 'стоп':

                print('\n#############################################################')
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
            print('\n******')
            print(f'Не успя да се сетиш {user.capitalize()} 😵')
            print(f'Преводът на "{random_word.upper()}" e "{target_word.upper()}"')
            total_errors += 1
            wrong_words.append(random_word)

            break

print('\nУспех с ученето на английския език!\n')
program_stop = input('Натисни "Enter за да затвориш програмата"')
record_session(user, total_translations, total_errors, wrong_words)