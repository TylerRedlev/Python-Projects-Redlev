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