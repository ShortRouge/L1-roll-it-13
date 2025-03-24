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


# main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")
