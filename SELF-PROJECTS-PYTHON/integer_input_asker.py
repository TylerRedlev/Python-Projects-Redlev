size = 0


def int_range_input(arg):

    while True:
        arg = input ("Please use an INTEGER value BIGGER THAN 0 for the size:")

        try:
            value_size = int(arg)
            print(value_size)
            arg = value_size
            print("Your value of size is {}".format(arg))
            if value_size <= 0:
                print("The value you entered is less than or equal to zero\n")
            else:
                print("Your distance between your bar and home is {} steps.".format(value_size))
                break
        except:
            print("The value you entered is not an integer \n")

    print(arg)


int_range_input(size)

print(size)
