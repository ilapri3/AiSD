def cathetus_2(a,b):
    try:
        assert str(a).isdigit() == True and str(b).isdigit() == True, 'invalid argument'
        assert b > a, 'cathetus must be less than hypotenuse'
        c = (b**2 - a**2)**0.5
        print(c)
    except AssertionError as err:
        print(err)
cathetus_2(3,5)