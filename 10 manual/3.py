def cathetus_2_():
    try:
        a = int(input('enter cathetus_1: '))
        b = int(input('enter hypothesis: '))
        assert b > a, 'cathetus must be less than hypotenuse'
        c = (b**2 - a**2)**0.5
        print(c)
    except AssertionError as err:
        print(err)
    except ValueError:
        print('invalid argument')

cathetus_2_()