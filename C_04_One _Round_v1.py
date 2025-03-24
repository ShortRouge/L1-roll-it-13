import random

# intialise rounds points
user_points = 0
comp_points = 0
double_user = "no"

# roll the dice for the user amd note if they got double
user_one = random.randint(1, 6)
user_two = random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"


# roll dice for computer
comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)

# update the user ? computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two

# output the results
print("\nInitial points")
print(f"user  - roll 1: {user_one} \t| roll 2: {user_two} \t| total: {user_points} ")
print(f"user  - roll 1: {user_one} \t| roll 2: {user_two} \t| total: {user_points} ")

# let the user know if they qualify for double points
if double_user == "yes":
    print("great news - if you win, you will earn double points!")