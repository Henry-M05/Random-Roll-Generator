import random
import numpy

# numpy.array()


class Roller:


    def __init__(self, success_chance : float, *, default_rolls = 1):
        self.successChance = success_chance
        self.defaultRolls = default_rolls

    '''
        roll_many rolls for a success or fail on the Roller's successChance. It does this for however many rolls are
    given in the num_rolls paramter. If num_rolls is left undefined, num_rolls is set to match the Roller's
    defaultRolls value.
    
        roll returns a numpy array of tuples in the format (successChance, success) where success is either true or 
    false.
    '''
    def roll_many(self, num_rolls : int = None):
        if num_rolls is None:
            num_rolls = self.defaultRolls

        roll_list = numpy.array((float, bool))
        roll_list.resize(num_rolls)

        for i in range(0,num_rolls):
            if random.random() <= self.successChance:
                roll_list[i] = (self.successChance, True)
            else:
                roll_list[i] = (self.successChance, False)

        return roll_list

    # roll rolls for a success or fail for a single roll of this Roller.
    def roll(self):
        return self.roll_many(num_rolls=1)[0]

    # Sets the default roll amount for this roller.
    # Has no return value.
    def set_default(self, new_default : int):
        self.defaultRolls = new_default



class RollerManager:
    rollerList = []

    def __getitem__(self, item):
        return self.rollerList[item]

    def add_roller(self, roller : Roller):
        self.rollerList.append(roller)

    def roll_all(self):
        listOfRolls = []
        for roller in self.rollerList:
            listOfRolls.append(roller.roll_many())

        return listOfRolls


    def all_roll_to_success(self, maxRolls):


        for roller in self.rollerList:
            successFound = False
            i = 0

            while i < maxRolls and successFound == False:
                if roller.roll()[1] == True:
                    successFound = True


    def individual_roll_to_success(self):
        pass