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


# main routine stars here
game_goal = int_cheak()
print(game_goal)
