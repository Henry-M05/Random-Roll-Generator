import biased_rolls


def main():
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

    print(rolls)




if __name__ == '__main__':
    main()