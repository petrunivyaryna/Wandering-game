"""This is the module for the wandering game in Lviv."""
class Location:
    """The class for setting up and describing the location."""
    def __init__(self, street: str):
        """
        This method has to set the name, the description of the street, the
        direction where you can go from this street, the character that you can meet
        here and the items that you can find.
        >>> krakivska.street
        'Вулиця Краківська'
        >>> krakivska.description
        'Дуже стара вулиця з великою кількістю історичних будівель та церков.'
        """
        self.street = street
        self.description = ''
        self.character = None
        self.items = None

    def set_description(self, description: str):
        """
        This method has to add the description of the street.
        >>> krakivska.set_description('Дуже стара вулиця з великою кількістю історичних будівель та церков.') 
        """
        self.description = description

    def set_character(self, character: object):
        """
        This method has to add character to the location.
        >>> krakivska.set_character(priest)
        """
        self.character = character

    def set_item(self, item: object):
        """
        This method has to add items to the location.
        >>> franko.set_item(flowers)
        """
        self.items = item

    def get_details(self):
        """
        This method has to print information about the room.
        >>> shevchenko.get_details()
        Вулиця Шевченка
        --------------------
        Одна з найвідоміших та найжвавіших вулиць у Львові
        """
        print(f"{self.street}\n--------------------\n{self.description}")
    
    def get_character(self):
        """
        This method has check whether there is enemy in the room and return None
        if there is not.
        >>> krakivska.get_character().name
        'Місцевий священник'
        >>> shevchenko.get_character().name
        'Група студентів'
        """
        return self.character

    def get_items(self):
        """
        This method has check whether there is item in the room and return None
        if there is not.
        >>> shevchenko.get_items().title
        'Монети'
        >>> franko.get_items().title
        'Букет'
        """
        return self.items

    def move(self, next_street):
        """
        This function has to change the room.
        """
        return next_street

    def get_name(self):
        """
        This function shoud return the nale of the street.
        >>> krakivska.get_name()
        'Вулиця Краківська'
        >>> kozelnytska.get_name()
        'Вулиця Козельницька'
        """
        return self.street


class Character:
    """This is the parent class for the Enemy class."""
    def __init__(self, name: str):
        """
        This method has to represent the character.
        >>> priest.name
        'Місцевий священник'
        >>> group_of_students.name
        'Група студентів'
        """
        self.name = name
        self.conversation = ''

    def set_conversation(self, conversation: str):
        """
        This method determines how the character will respond to an attempt to talk to him.
        >>> priest.conversation
        'Привіт! Я можу дати тобі аптечку.'
        >>> kavaler.conversation
        'Я маю букет для тебе.'
        """
        self.conversation = conversation

    def describe(self):
        """
        This method has to print information about the character in the room.
        # >>> priest.describe
        # >>> kavaler.describe
        """
        print(f"{self.name} is here!")

    def talk(self):
        """
        This method represents the words of the enemy.
        """
        print(f"[{self.name} says]: {self.conversation}")


class Enemy(Character):
    """This is a child class for the Character class."""
    def __init__(self, name: str):
        """
        Inherits the name and conversation attributes from the parent class.
        >>> group_of_students.name
        'Група студентів'
        """
        super().__init__(name)

    def set_conversation(self, conversation: str):
        """
        This method has to add the characteristic of the Character.
        >>> group_of_students.set_conversation("Ти мені наступив на ногу! Як можна було бути \
таким необачним? Не бачиш, що тут люди стоять?")
        """
        return super().set_conversation(conversation)

    def describe(self):
        """
        This method should return the description of the character.
        >>> batar.describe()
        Батяр is here!
        """
        return super().describe()

    def set_weakness(self, weakness: str):
        """
        This method has to determine the weakness of the enemy.
        >>> batar.set_weakness(monets.get_name())
        """
        self.weakness = weakness

    def talk(self):
        """
        This function shoud return replica of the character.
        >>> group_of_students.talk()
        [Група студентів says]: Ти мені наступив на ногу! Як можна було \
бути таким необачним? Не бачиш, що тут люди стоять?
        """
        return super().talk()

    def fight(self, weapon: str):
        """
        This method should check whether we can beat our enemy with this weapon.
        >>> batar.fight('Монети')
        True
        """
        if self.weakness == Weapon(weapon).title:
            # Enemy.defeated_count += 1
            return True
        return False

class Item:
    """This is the parent class for the Weapon and Support classes."""
    def __init__(self, title: str):
        """
        This method has to determine the item and the description of it.
        >>> monets.title
        'Монети'
        >>> flowers.title
        'Букет'
        >>> flowers.appearance
        'Букет червоних троянд.'
        """
        self.title = title
        self.appearance = ''

    def set_description(self, appearance):
        """
        This method has to add the characteristic of the Item.
        >>> flowers.set_description('Букет червоних троянд.')
        """
        self.appearance = appearance

    def describe(self):
        """
        This method has to print information about the item in the room.
        """
        print(f"[{self.title}] is here - {self.appearance}")

    def get_name(self):
        """
        This method should return the name of the item.
        >>> flowers.get_name()
        'Букет'
        """
        return self.title

class Weapon(Item):
    """This is a child class for the Item class."""
    def __init__(self, title: str):
        """
        This method has to determine the item and the description of it.
        >>> monets.title
        'Монети'
        >>> monets.appearance
        'На дорозі ти побачив монети, вони зможуть знадобитися тобі потім.'
        """
        super().__init__(title)

    def set_description(self, appearance):
        """
        This method has to add the characteristic of the Item.
        >>> monets.set_description('На дорозі ти побачив монети, \
вони зможуть знадобитися тобі потім.')
        """
        return super().set_description(appearance)

    def describe(self):
        """
        This function should return the description of the weapon item.
        >>> monets.describe()
        [Монети] is here - На дорозі ти побачив монети, вони зможуть знадобитися тобі потім.
        """
        return super().describe()
    
    def get_name(self):
        """
        This function should return the name of the Item.
        >>> monets.get_name()
        'Монети'
        """
        return super().get_name()


class Support(Item):
    """This is a child class for the Item class."""
    def __init__(self, title: str):
        """
        This method has to determine the item and the description of it.
        >>> first_aid_kit.title
        'Аптечка'
        >>> first_aid_kit.appearance
        'Предмет, який зможе врятувати твоє життя.'
        """
        super().__init__(title)

    def set_description(self, appearance):
        """
        This method has to add the characteristic of the Item.
        >>> first_aid_kit.set_description("Предмет, який зможе врятувати твоє життя.")
        """
        return super().set_description(appearance)

    def describe(self):
        """
        This function should describe the support item.
        >>> first_aid_kit.describe()
        [Аптечка] is here - Предмет, який зможе врятувати твоє життя.
        """
        return super().describe()


# Location №1
krakivska = Location('Вулиця Краківська')
krakivska.set_description('Дуже стара вулиця з великою кількістю історичних будівель та церков.')

priest = Character("Місцевий священник")
priest.set_conversation("Привіт! Я можу дати тобі аптечку.")
krakivska.set_character(priest)

first_aid_kit = Support("Аптечка")
first_aid_kit.set_description("Предмет, який зможе врятувати твоє життя.")
krakivska.set_item(first_aid_kit)

# Location №2
shevchenko = Location('Вулиця Шевченка')
shevchenko.set_description('Одна з найвідоміших та найжвавіших вулиць у Львові')

group_of_students = Enemy('Група студентів')
group_of_students.set_conversation("Ти мені наступив на ногу! Як можна було бути \
таким необачним? Не бачиш, що тут люди стоять?")
# group_of_students.set_weakness(spray_bottle)
shevchenko.set_character(group_of_students)

monets = Item('Монети')
monets.set_description('На дорозі ти побачив монети, вони зможуть знадобитися тобі потім.')
shevchenko.set_item(monets)

# Location №3
franko = Location('Вулиця Франка')
franko.set_description("Одна з центральних вулиць Львова, яка славиться своєю популярністю серед туристів.")

kavaler = Character('Кавалер')
kavaler.set_conversation('Я маю букет для тебе.')
franko.set_character(kavaler)

flowers = Item('Букет')
flowers.set_description('Букет червоних троянд.')
franko.set_item(flowers)

# Location №4
stryska = Location('Вулиця Стрийська')
stryska.set_description("Вулиця виглядає дуже непривітно у цей час. Здається тут небезпечно...")

batar = Enemy('Батяр')
batar.set_conversation('Якщо хочеш пройти далі, заплати мені.')
batar.set_weakness(monets.get_name())
stryska.set_character(batar)

# Location №5
kozelnytska = Location('Вулиця Козельницька')
kozelnytska.set_description('Нарешті ти пройшов до колегіуму. Але як зробити так, щоб куратор тебе впустив???')

kyrator = Enemy('Куратор')
kyrator.set_conversation('Ти запізнився на 30 хв. Доганааа!!!')
kyrator.set_weakness(flowers.get_name())
kozelnytska.set_character(kyrator)

keys = Item('Ключі від кімнати')
keys.set_description('Ураа! Нарешті я можу піти в кімнату спати.')
kozelnytska.set_item(keys)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
