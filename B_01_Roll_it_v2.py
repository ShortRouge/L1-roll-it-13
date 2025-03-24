# functions go here

def yes_no(question):
    """cheak user response to a question is yes / no (y/n), return 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # cheak if user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """print instructions"""

    print("""
*** instructions ****

Roll the dice and try win
    """)


def int_cheak():
    """cheak users enter an integer more than / equal to 13"""

    error = "please enter an integer more than / equal to 13. "

    while True:
        try:
            response = int(input("what is game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_cheak()
print(game_goal)
