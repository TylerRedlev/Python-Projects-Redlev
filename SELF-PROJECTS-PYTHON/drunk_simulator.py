from random import randint

#   Imported random library of Python
"""
    DRUNK SIMULATOR 1.0
    -------------------

    Drunk Simulator program is a little exercise which can be a fun little brain teaser
    for Python enthusiast who want to practice their understanding of basic Python functionalities
    while being able to get acquainted with fundamental computer science concepts such as loops,
    conditional statements, variables, arrays etc..

    THE TASK:
    ---------

    You've had a few drinks at the bar. Seems like you're not too good with handling the booze,
    because you're drunk. We'll see if you're able to get home or end up somewhere else.

    Your task is to write a program which will involve creating a function with 2 arguments:
    drunkman_simulator(size, steps)

    In this function you'll provide 2 arguments which are size and steps.
    Size: The distance between bar and home.
    Steps: How many steps will you step forward in order to reach your home.

    You will start your journey from the mid-point. Right between your bar and your home.
    Each step will be randomly stepped either to the direction of home or the bar, which
    you will be determining by a random number generation( between 0-10 or 0-100, it's up to you).
    In each step your location will be recorded and your location will be printed:
    home.....*.....pub
    home......*....pub
    home.....*.....pub
    home....*......pub
    home...*.......pub
    home....*......pub

    And when you reach your final step, the program should print whether you're at home, at the bar
    or fell asleep somewhere in between. As example:

    You've reached the pub.. Again.. You drunkard..
    You arrived home. At least you have some responsibility...
    You fell asleep on the street.. Pathetic.

    You don't have to stick to my code, feel free to improve it :)
"""

"""
|--------------------------------------------------------------------------
| GREETING AND GLOBAL VARIABLES
|--------------------------------------------------------------------------
"""

#   Defining the global variables

greeting = "*-------------------*\n  WELCOME TO DRUNK SIMULATOR 1.0\n*-------------------*"

print(greeting)
print("Please enter a size for the distance between the bar and your home.\n")

size_message = "Please use an INTEGER value BIGGER THAN 0 for the size:"
steps_message = "Please enter an INTEGER value BIGGER THAN 0 for the steps you will take:"
home = "home"
pub = "pub"

"""
|--------------------------------------------------------------------------
| SIZE INPUT LOOP AND FILTRATION FOR INTEGER VALUES
|--------------------------------------------------------------------------
"""
while True:
    size = input(size_message)

    try:
        value_size = int(size)
        print(value_size)
        if value_size <= 0:
            print("The value you entered is less than or equal to zero\n")
        else:
            print("Your distance between your bar and home is {} steps.".format(value_size))
            size = value_size
            break
    except:
        print("The value you entered is not an integer \n")

"""
|--------------------------------------------------------------------------
| LOOP FOR STEPS INPUT
|--------------------------------------------------------------------------
"""
while True:
    steps = input(steps_message)

    try:
        value_steps = int(steps)
        print(value_steps)
        if value_steps <= 0:
            print("The value you entered is less than or equal to zero\n")
        else:
            print("You will step {} steps. Let's see how it goes...".format(value_steps))
            steps = value_steps
            break;
    except:
        print("The value you entered is not an integer \n")

"""
|--------------------------------------------------------------------------
| FUNCTION DEFINITION
|--------------------------------------------------------------------------
"""


def drunkman_simulator(size, steps):
    i = 1
    point = int(size / 2)

    """
        |--------------------------------------------------------------------------
        | THE LOOP
        |--------------------------------------------------------------------------
        """

    while i < steps:
        home_distance = "." * int(point)
        pub_distance = "." * int((size - point))
        moment = [home, home_distance, "*", pub_distance, pub]
        step_side = randint(0, 100)

        if point == 0:
            print("".join(moment))
            print("You've reached home")
            return

        elif point == size:
            print("".join(moment))
            print("You've reached the pub..")
            return

        if step_side < 50:
            point = point - 1
            print("".join(moment))

        elif step_side >= 50:
            point = point + 1
            print("".join(moment))

        i += 1
        pass


drunkman_simulator(size, steps)
