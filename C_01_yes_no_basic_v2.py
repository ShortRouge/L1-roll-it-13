
# functions go here

def yes_no(question):

    """cheak user response to a question is yes / no (y/n), return 'yes' or 'no' """

    while True:

        response = input(question).lower()

        #cheak if user says yes / no
        if response == "yes" or response == "y":
           return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

# main routine

#testing loop...
while True:
    want_instructions = yes_no("do you want to see the instructions")
    print(f"you chose {want_instructions}")

print("we done")
