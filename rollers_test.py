import numpy

import biased_rolls


def main():
    numpy.set_printoptions(threshold=80000)

    manager = biased_rolls.RollerManager()

    roller1 = biased_rolls.Roller(1/10, default_rolls = 100)
    roller2 = biased_rolls.Roller(1/200)
    roller3 = biased_rolls.Roller(0, default_rolls=20)
    roller4 = biased_rolls.Roller(1, default_rolls=100)

    manager.add_roller(roller1)
    manager.add_roller(roller2)
    manager.add_roller(roller3)
    manager.add_roller(roller4)

    rolls = manager.roll_all()

    # manager.display_rollers()

    # roller2_success = manager.individual_roll_to_success(20000,1)
    # print(roller2_success)

    # print(manager.all_roll_to_success(20000))
    # print(rolls)

    manager2 = biased_rolls.RollerManager()
    roller5 = biased_rolls.Roller(1/8000)

    manager2.add_roller(roller5)

    roll_list = numpy.array((float,int))
    roll_list.resize(5000)

    manager2.display_rollers()

    for i in range(0,5000):
        roll_list[i] = (manager2.individual_roll_to_success(20000,0))

    print(roll_list)





if __name__ == '__main__':
    main()