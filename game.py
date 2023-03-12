"""This is the module for the wandering games."""
class Room:
    """The class for setting up and describing a room."""
    def __init__(self, room: str):
        """
        This method has to set the name of the room, the description and the
        directions where you can go from this room, characters and items in this room.
        >>> kitchen.room
        'Kitchen'
        >>> kitchen.description
        'A dank and dirty room buzzing with flies.'
        >>> dining_hall.room
        'Dining Hall'
        """
        self.room = room
        self.description = ''
        self.directions = {}
        self.character = None
        self.item = None

    def set_description(self, description: str):
        """
        This method has to add the description of the room.
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        """
        self.description = description

    def link_room(self, next_room: object, direction: str):
        """
        This method has to create a dictionary that represents the relationship between rooms.
        >>> kitchen.link_room(dining_hall, "south")
        """
        self.directions.update({next_room: direction})

    def set_character(self, character: object):
        """
        This method has to add characters to the room.
        >>> dining_hall.set_character(dave)
        """
        self.character = character

    def set_item(self, item: object):
        """
        This method has to add item to the room.
        >>> ballroom.set_item(cheese)
        >>> dining_hall.set_item(book)
        """
        self.item = item

    def get_details(self):
        """
        This method has to print information about the room.
        >>> current_room.get_details()
        Kitchen
        --------------------
        A dank and dirty room buzzing with flies.
        The Dining Hall is south
        >>> ballroom.get_details()
        Ballroom
        --------------------
        A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.
        The Dining Hall is east
        """
        print(f"{self.room}\n--------------------\n{self.description}")
        for ways in self.directions.items():
            print(f"The {ways[0].room} is {ways[1]}")

    def get_character(self):
        """
        This method has check whether there is enemy in the room and return None
        if there is not.
        >>> current_room.get_character()
        """
        return self.character

    def get_item(self):
        """
        This method has check whether there is item in the room and return None
        if there is not.
        >>> current_room.get_item()
        """
        return self.item

    def move(self, command):
        """
        This function has to change the room.
        """
        for way in self.directions.items():
            if way[1] == command:
                next_room = way[0]
                # self.__dict__.update(next_room.__dict__)
                return next_room
        return self


class Enemy:
    """The class for representing and describing an enemy."""
    defeated_count = 0
    def __init__(self, name: str, characteristic: str):
        """
        This method has to reoresent the enemy by his name and characteristic.
        >>> dave.name
        'Dave'
        >>> dave.characteristic
        'A smelly zombie'
        >>> dave.conversation
        "What's up, dude! I'm hungry."
        >>> dave.weakness
        'cheese'
        >>> tabitha.name
        'Tabitha'
        >>> tabitha.characteristic
        'An enormous spider with countless eyes and furry legs.'
        >>> tabitha.conversation
        "Sssss....I'm so bored..."
        >>> tabitha.weakness
        'book'
        """
        self.name = name
        self.characteristic = characteristic
        self.conversation = ''
        self.weakness = ''

    def set_conversation(self, conversation: str):
        """
        This method determines how the character will respond to an attempt to talk to him.
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str):
        """
        This method has to determine the weakness of the enemy.
        >>> dave.set_weakness("cheese")
        """
        self.weakness = weakness

    def describe(self):
        """
        This method has to print information about the character in the room.
        >>> ballroom.get_character().describe()
        Tabitha is here!
        An enormous spider with countless eyes and furry legs.
        """
        print(f"{self.name} is here!\n{self.characteristic}")

    def talk(self):
        """
        This method represents the words of the enemy.
        >>> ballroom.get_character().talk()
        [Tabitha says]: Sssss....I'm so bored...
        """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, weapon: str):
        """
        This method should check whether we can beat our enemy with this weapon.
        """
        if self.weakness == Item(weapon).title:
            Enemy.defeated_count += 1
            return True
        return False

    def get_defeated(self):
        """
        Should return the number of victories.
        >>> ballroom.get_character().get_defeated()
        0
        """
        return Enemy.defeated_count


class Item:
    """The class for representing and describing the item to fight the enemy."""
    def __init__(self, title: str):
        """
        This method has to determine the item and the description of it.
        >>> cheese.title
        'cheese'
        >>> cheese.appearance
        'A large and smelly block of cheese'
        >>> book.title
        'book'
        >>> book.appearance
        "A really good book entitled 'Knitting for dummies'"
        """
        self.title = title
        self.appearance = ''

    def set_description(self, appearance):
        """
        This method has to add the characteristic of the Item.
        >>> cheese.set_description("A large and smelly block of cheese")
        """
        self.appearance = appearance

    def describe(self):
        """
        This method has to print information about the item in the room.
        >>> ballroom.get_item().describe()
        The [cheese] is here - A large and smelly block of cheese
        """
        print(f"The [{self.title}] is here - {self.appearance}")

    def get_name(self):
        """
        This method should return the name of the item.
        >>> ballroom.get_item().get_name()
        'cheese'
        """
        return self.title

# Rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. \
Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")

dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

ballroom.link_room(dining_hall, "east")

# Enemy №1
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# Enemy №2
tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

# Item №1
cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

# Item №2
book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

# How to get details
current_room = kitchen
current_room.get_details()
ballroom.get_character() # has to be the object
ballroom.get_character().describe()
current_room.get_item() # has to return None because there is any items.
ballroom.get_item().describe()
ballroom.get_character().talk()
# adds an extra win in the main game
# ballroom.get_character().fight('book') 
ballroom.get_character().get_defeated()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
