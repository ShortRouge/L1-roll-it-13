import random


def yes_no(question):
    """cheak user response to a question is yes / no (y/n), return 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check if user says yes / no
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


def int_check():
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


def initial_points(which_players, ):
    """roll dice twice and return total / if double pints apply"""

    double = "no"

    # roll the dice for the user amd note if they got double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_one
    print(f"{which_players} - roll 1: {roll_one} \t| roll 2: {roll_two} \t| total: {total} ")

    return total, double


def make_statement(statement, decoration):
    """add emoji / additional characters to the end"""

    end = decoration * 3
    print(f"\n{end} {statement} {end}")


# main starts here...

# at the start of the game , the computer / user score are both zero
comp_score = 0
user_score = 0
round_played = 0

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()

game_history = []

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    round_played += 1

    # start of round loop
    make_statement(f"round {round_played}", "🎲")

    # roll the dice for user and note if they got a double
    initial_user = initial_points("user")
    initial_comp = initial_points("comp")

    # retrieve user points (first item returned from function)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # let the user know if they qualify for double points
    if double_user == "yes":
        print("great news - if you win, you will earn double points!")

    # assume_user goes first
    first = "user"
    second = "computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer point, they start the game
    if user_points < comp_points:
        print("you start because your initial roll was less than the computer\n")

    # if the user and computer roll equal points, the user is player 1...
    elif user_points == comp_points:
        print("the initial roll were the same, the user starts!")

    # if the computer has fewer points . switch the computer to "player 1"
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # loop until we have a winner...
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round\n")

        # first person rolls the dice and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points} | {second} {player_2_points}")

    # end of rounds

    # associate player points with either the user or computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if first == "computer":
        user_points, comp_points = comp_points, user_points

    # work out who won and set the loser's points to zero
    if user_points > comp_points:

        winner = "user"
        loser = "user"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"the {winner} won. the {loser}'s points have been reset to zero"

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # Output round results
    make_statement("round results", "=")
    print(f"user points: {user_points} | computer points: {comp_points}")
    print(round_feedback)
    print()

    # outside round loop - update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # generate round results and add it to the game history list
    game_results = (f"round {round_played}: user points {user_points} | "
                    f"computer points {comp_points}, {winner} wins (15 | 0)"
                    f"{user_score} | {comp_score})")

    game_history.append(game_results)

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")  # replace with call to statement generator
    print(f"user score: {user_score} | computer score {comp_score}")

# end of entire game, output final results

make_statement("game over", "👍")

print()
if user_score > comp_score:
    make_statement("the user won", "👍")  # replace this with statement generator call
else:
    make_statement("the computer won", "💻")

print("game history")

for item in game_history:
    print(item)
