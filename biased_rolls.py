import random
import numpy



class Roller:

    def __init__(self, success_chance : float, *, default_rolls = 1):
        self.successChance = success_chance
        self.defaultRolls = default_rolls

    '''
    roll_many rolls for a success or fail on the Roller's successChance. It does this for however many rolls are
    given in the num_rolls paramter. If num_rolls is left undefined, num_rolls is set to match the Roller's
    defaultRolls value.
    
    roll_many returns a numpy array of tuples in the format (successChance, success) where success is either true or 
    false.
    '''
    def roll_many(self, num_rolls : int = None):
        if num_rolls is None:
            num_rolls = self.defaultRolls

        roll_list = numpy.array((float, bool))
        roll_list.resize(num_rolls)

        for i in range(0,num_rolls):
            if random.random() < self.successChance:
                roll_list[i] = (self.successChance, True)
            else:
                roll_list[i] = (self.successChance, False)

        return roll_list

    '''
    roll rolls for a success or fail for a single roll of this Roller.
    
    roll returns a tuple of the format (successChance, success) where success is a boolean.
    '''
    def roll(self):
        return self.roll_many(num_rolls=1)[0]

    # Sets the default roll amount for this roller.
    # Has no return value.
    def set_default(self, new_default : int):
        self.defaultRolls = new_default


class RollerManager:
    def __init__(self):
        self.rollerList = []

    def __getitem__(self, item):
        return self.rollerList[item]

    def add_roller(self, roller : Roller):
        self.rollerList.append(roller)

    def display_rollers(self):
        i = 0
        for roller in self.rollerList:
            print(f"|r{i}: {roller.successChance}|", end=" ")
            i += 1
        print()

    def roll_all(self):
        list_of_rolls = []
        for roller in self.rollerList:
            list_of_rolls.append(roller.roll_many())

        return list_of_rolls

    def individual_roll_to_success(self, max_rolls: int, index: int):
        roller = self.rollerList[index]

        for i in range(0, max_rolls):
            if roller.roll()[1] is True:
                return (roller.successChance, i+1)
        return (roller.successChance, -1)

    '''
    all_roll_to_success rolls each roller (to a maximum of maxRolls times) until a successful roll is had.

    all_roll_to_success returns a list of tuples in the format (successChance, steps) where successChance is the chance
    that a given roller had to succeed, and steps is the amount of rolls it took to succeed. If the roller never
    succeeded, steps will instead by -1.
    '''
    def all_roll_to_success(self, max_rolls: int):

        roll_results = []

        for i in range (0, len(self.rollerList)):
            roll_results.append(self.individual_roll_to_success(max_rolls, i))

        return roll_results


