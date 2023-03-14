import my_game
# Locations:

# Location №1
krakivska = my_game.Location('Вулиця Краківська')
krakivska.set_description('Дуже стара вулиця з великою кількістю історичних будівель та церков.')

priest = my_game.Character("Місцевий священник")
priest.set_conversation("Привіт! Я можу дати тобі аптечку.")
krakivska.set_character(priest)

first_aid_kit = my_game.Support("Аптечка")
first_aid_kit.set_description("Предмет, який зможе врятувати твоє життя.")
krakivska.set_item(first_aid_kit)

# Location №2
shevchenko = my_game.Location('Вулиця Шевченка')
shevchenko.set_description('Одна з найвідоміших та найжвавіших вулиць у Львові')

group_of_students = my_game.Enemy('Група студентів')
group_of_students.set_conversation("Ти мені наступив на ногу! Як можна було бути \
таким необачним? Не бачиш, що тут люди стоять?")
# group_of_students.set_weakness(spray_bottle)
shevchenko.set_character(group_of_students)

monets = my_game.Item('Монети')
monets.set_description('На дорозі ти побачив монети, вони зможуть знадобитися тобі потім.')
shevchenko.set_item(monets)

# Location №3
franko = my_game.Location('Вулиця Франка')
franko.set_description("Одна з центральних вулиць Львова, яка славиться своєю популярністю серед туристів.")

kavaler = my_game.Character('Кавалер')
kavaler.set_conversation('Я маю букет для тебе.')
franko.set_character(kavaler)

flowers = my_game.Item('Букет')
flowers.set_description('Букет червоних троянд.')
franko.set_item(flowers)

# Location №4
stryska = my_game.Location('Вулиця Стрийська')
stryska.set_description("Вулиця виглядає дуже непривітно у цей час. Здається тут небезпечно...")

batar = my_game.Enemy('Батяр')
batar.set_conversation('Якщо хочеш пройти далі, заплати мені.')
batar.set_weakness(monets.get_name())
stryska.set_character(batar)

# Location №5
kozelnytska = my_game.Location('Вулиця Козельницька')
kozelnytska.set_description('Нарешті ти пройшов до колегіуму. Але як зробити так, щоб куратор тебе впустив???')

kyrator = my_game.Enemy('Куратор')
kyrator.set_conversation('Ти запізнився на 30 хв. Доганааа!!!')
kyrator.set_weakness(flowers.get_name())
kozelnytska.set_character(kyrator)

keys = my_game.Item('Ключі від кімнати')
keys.set_description('Ураа! Нарешті я можу піти в кімнату спати.')
kozelnytska.set_item(keys)

current_location = krakivska
backpack = {'Support': [], 'Weapon': []}
locations = [krakivska, shevchenko, franko, stryska, kozelnytska]

dead = False
print('Ти граєш за студента УКУ, який загубився у центрі Львова.\n\
На годиннику 22:30, тобі потрібно добратися до колегіуму УКУ на вулиці \
Козельницькій, де тебе чекає злий куратор...')

while dead == False:

    print("\n")
    current_location.get_details()

    inhabitant = current_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    items = current_location.get_items()
    # if items:
    if inhabitant is not None:
        if not isinstance(inhabitant, my_game.Enemy):
            print('Ти можеш поговорити із незнайомцем або піти далі.')
            print(f'Наступна вулиця: {locations[locations.index(current_location) + 1].get_name()}')
            print('Введи число: 1-поговорити, 2-наступна вулиця')
            command = input("> ")
            if command == "1":
            # Talk to the inhabitant - check whether there is one!
                if inhabitant is not None:
                    inhabitant.talk()
                    items.describe()
                    command = input("Якщо хочеш взяти предмет введи цифру 1: ")
                    if command == '1':
                        if items is not None:
                            print("Ти поклав " + items.get_name() + " у свій рюкзак.")
                            if isinstance(items, my_game.Support):
                                backpack['Support'].append(items.get_name())
                                current_location.set_item(None)
                            else:
                                backpack['Weapon'].append(items.get_name())
                                current_location.set_item(None)
                        else:
                            print('Тут немає ніякого предмету')
                            current_location = current_location.move(locations[locations.index(current_location) + 1])
                    current_location.set_character(None)
                    current_location = current_location.move(locations[locations.index(current_location) + 1])
            elif command == '2':
                # Move to another street
                current_location = current_location.move(locations[locations.index(current_location) + 1])
            else:
                print('Немає команди ' + command)

        else: # Inhabitant is our enemy
            inhabitant.talk()
            print('Здається тут небезпечно... Тобі потрібно здолати ворога!')
            # Fight with the inhabitant
            if not backpack['Weapon']:
                print('Але тобі немає чим битися... Ти програв')
                if backpack['Support']:
                    print('У мене є хороші новини: у тебе є аптечка!')
                    command = input('Якщо хочеш вилікуватися введи цифру 1: ')
                    if command == '1':
                        print('Вітаю. Ти можеш переходити на нову вулицю, але будь обережним, тепер у тебе немає аптечки...')
                        backpack['Support'].remove('Аптечка')
                        if items:
                            items.describe()
                            command = input("Якщо хочеш взяти предмет введи цифру 1: ")
                            if command == '1':
                                if items is not None:
                                    print("Ти поклав " + items.get_name() + " у свій рюкзак.")
                                    if isinstance(items, my_game.Support):
                                        backpack['Support'].append(items.get_name())
                                        current_location.set_item(None)
                                    else:
                                        backpack['Weapon'].append(items.get_name())
                                        current_location.set_item(None)
                        current_location = current_location.move(locations[locations.index(current_location) + 1])
                else:
                    print("Здається ти вже не живеш у колегіумі...")
                    dead = True
            else:
                print('Тобі потрібно вибрати чим ти хочеш боротися.')
                print(f"Ось твоя зброя: {backpack['Weapon']}")
                fight_with = input("Обери предмет: ")
                if fight_with in backpack['Weapon']:

                    if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                        print("Ти виграв бійку!")
                        current_location.character = None
                        backpack['Weapon'].remove(fight_with)
                        if current_location == kozelnytska:
                            print('Ти впорався із завданням.')
                            print("Ти нарешті в колегіумі!")
                            dead = True
                        else:
                            if items:
                                items.describe()
                                command = input("Якщо хочеш взяти предмет введи цифру 1: ")
                                if command == '1':
                                    if items is not None:
                                        print("Ти поклав " + items.get_name() + " у свій рюкзак.")
                                        if isinstance(items, my_game.Support):
                                            backpack['Support'].append(items.get_name())
                                            current_location.set_item(None)
                                        else:
                                            backpack['Weapon'].append(items.get_name())
                                            current_location.set_item(None)
                            current_location = current_location.move(locations[locations.index(current_location) + 1])

                    else:
                        # What happens if you lose?
                        print("Ти не зміг перемогти у цій бійці")
                        print("Здається ти вже не живеш у колегіумі...")
                        dead = True
                else:
                    print("Ти не маєш " + fight_with)
