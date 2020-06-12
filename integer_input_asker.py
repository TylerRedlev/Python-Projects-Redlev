


def int_range_inputter():

    while True:
        the_size = input ("Please use an INTEGER value BIGGER THAN 0 for the size:")

        try:
            value_size = int(the_size)
            print(value_size)
            if (value_size <= 0):
                print("The value you entered is less than or equal to zero\n")
            else:
                print("Your distance between your bar and home is {} steps.".format(value_size))
                break;
        except:
            print("The value you entered is not an integer \n")

    print("This is outside the loop boundaries. Your size is {}".format(value_size))