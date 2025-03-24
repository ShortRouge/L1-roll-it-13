# at the start of the game , the computer / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("game goal"))      # should be function call!

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # start of round loop
    # for testing purposes, ask the user what the point for the user / computer were
    comp_points = int(input("enter the computer points at the end of the round: "))
    user_points = int(input("enter the users points at the end of the round"))

    # outside round loop - update score with round round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")    # replace with call to statement generator
    print(f"user score: {user_score} | computer score {comp_score}")


# end of entire game, output final results
print()
if user_score > comp_score:
    print("the user won")   # replace this with statement generator call
else:
    print("the computer won")
