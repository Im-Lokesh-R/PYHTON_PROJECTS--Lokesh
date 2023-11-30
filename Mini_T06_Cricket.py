# MINI  T06  CRICKET GAME CREATED BY LOKESH

import random

input("press enter to continue......  :)")

print("welcome to our mini T06 cricket game ..hope you enjoy this ..")

#team choosing

team=("CSK","MI","RCB","GT","DC","KKR","LSG","PK","RR","SRH")
print("CSK","MI","RCB","GT","DC","KKR","LSG","PK","RR","SRH")
user_team=input("chose your team(every letters in caps)==".upper())
opponant_team=random.choice(team)
print(f"your opponent is {opponant_team}")

input("REMEMBER THAT THIS GAME HAS ONLY SIX OVER IT'S MEAN YOU ONLY GOT 36 BALL TO PLAY..ENTER TO CONTINUE")
input("NOTE: DONT TRY TO PUT MORE THAN 6 NUMBERS  ... ENTER TO CONTINUE")
input("it.s time for the toss")
user = input("choose heads or tails(lowercase)==".lower())
input("now tossing the coin .....")


# toss space
toss = ("heads", "tails")
role = ("bat", "bowl")
numbers=[1,2,3,4,5,6]
random_toss = random.choice(toss)
random_opponent = random.choice(role)
print(f"and it's {random_toss}")

# role choice
if user == random_toss:
    input(" fantastic you won the toss...enter to continue")
    user_input = input(f"Now what is {user_team} role in the first half  BAT OR BOWL ....==".lower())
# user toss win
    if user_input == "bat":
        input("NOTE:"
              "      GAME RULES"
              "        FOR BOWLING OR BATTING YOU SHOULD ENTER NUMBER BETWEEN 1 TO 6 ......"
              "        LET'S START  ")
        user_score=0
        print(f"{user_team} batting and  {opponant_team} is bowling")
#USER BATTING AREA(innings1)
        print("its a first half")
        for i in range(36):
            user_choice =int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if user_choice == random_numbers:
                print(f"{user_team} out by putting the same number has your {opponant_team}")
                input(f"now the first half is overr and {user_team} score is= {user_score}.. enter to continue ")
                input(f"try to defend {opponant_team} by without taking more than {user_score}")
                break
            else:
                user_score +=int(user_choice)
                print(f"{user_team} score {user_score}")
                continue

        input(f"now the first half is overr and {user_team} score is= {user_score}.. enter to continue ")
        input(f"try to defend {opponant_team} by without taking more than {user_score}")
#USER BOWLING AREA(innings 2)
        print("it is second half ")
        print(f"{user_team} bowling and {opponant_team} is batting")
        opponent_score=0
        for i in range(36):
            user_choice = int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if random_numbers == user_choice:
                print(f"{opponant_team} got out by {user_team} bowling ")
                if user_choice>=opponent_score:
                    print(f"{user_team} WON BY  DEFENDING YOUR SCORE AGAINST {opponant_team}")
                    input(f"congrat {user_team} won >>>>>>>>>")
                elif opponent_score == user_score:
                    print("it's a tie")
                else:
                    input(f"{user_team} lost<<<<<<<")
                    print(f"{opponant_team} WIN BY TAKING MORE SCORE THAN {user_team}")
                break
            else:
                opponent_score += int(random_numbers)
                print(f"{opponant_team} score {opponent_score}")
                if opponent_score>user_score:
                    input(f"{user_team} lost<<<<<<<")
                    print(f"{opponant_team} WIN BY TAKING MORE SCORE THAN {user_team}")
                    exit()
                elif opponent_score == user_score:
                    print("it's a tie")
                    continue
                else:
                    continue
                continue
#USER BOWLING AREA(innings 1)
    elif user_input=="bowl":
        input("NOTE:"
              "      GAME RULES"
              "        FOR BOWLING OR BATTING YOU SHOULD ENTER NUMBER BETWEEN 1 TO 6 ......"
              "        LET'S START  ")
        opponent_score = 0
        print(f"{user_team} bowling and {opponant_team} is batting")
        print("its a first half")

        for i in range(36):
            user_choice = int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if random_numbers == user_choice:
                print(f"{opponant_team} got out by your bowling ")
                input(f"now the first half is overr and {opponant_team} score is= {opponent_score}.. enter to continue ")
                input(f"try to get more score than {opponant_team} score by  taking more than {opponent_score}")
                break
            else:
                opponent_score += int(random_numbers)
                print(f"{opponant_team} score {opponent_score}")
                continue

        input(f"now the first half is overr and {opponant_team} score is= {opponent_score}.. enter to continue ")
        input(f"try to get more score than {opponant_team} score by  taking more than {opponent_score}")
#USER BATTING AREA (inings 2)
        print(f"{user_team} batting and {opponant_team} is bowling")
        user_score=0
        print("it is second half ")
        for i in range(36):
            user_choice =int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if user_choice == random_numbers:
                print(f"{user_team} out by putting the same number has  {opponant_team}")
                if user_choice>=opponent_score:
                    print(f"{user_team} WON BY TAKING MORE SCORE THAN {opponant_team}")
                    input(f"congrat {user_team} won >>>>>>>>>")
                elif user_score == opponent_score:
                    print("it's a tie")
                else:
                    input(f"{user_team} lost<<<<<<<")
                    print(f"{opponant_team} WIN BY DEFENDING HIS SCORE")
                break
            else:
                user_score +=int(user_choice)
                print(f"{user_team} score {user_score}")
                if user_score>opponent_score:
                    print(f"{user_team} WON BY TAKING MORE SCORE THAN {opponant_team}")
                    input(f"congrat {user_team} won >>>>>>>>>")
                    exit()
                elif user_score == opponent_score:
                    print("it's a tie")
                    continue
                else:
                    continue
                continue
    else:
        print("try to put every thing in lower case")
#opponent toss win
else:
    input(f"{opponant_team} won the toss and... enter to continue")
    print(f" choosed to {random_opponent}")
#OPPONENT BOWLING AREA(innings 1)
    if random_opponent == "bowl":
        input("NOTE:"
              "      GAME RULES"
              "        FOR BOWLING OR BATTING YOU SHOULD ENTER NUMBER BETWEEN 1 TO 6 ......"
              "        LET'S START  ")
        user_score=0
        print(f"{user_team} batting and {opponant_team} is bowling")
        print("its a first half")

        for i in range(36):
            user_choice = int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if user_choice == random_numbers:
                print(f"{user_team} out by putting the same number has {opponant_team}")
                input(f"now the first half is overr and {user_team} score is= {user_score}.. enter to continue ")
                input(f"try to defend {user_team} score by without taking more than {user_score}")
                break
            else:
                user_score +=int(user_choice)
                print(f"{user_team} score {user_score}")
                continue

        input(f"now the first half is overr and {user_team} score is= {user_score}.. enter to continue ")
        input(f"try to defend {opponant_team} score by without taking more than {user_score}")
#OPPONENT BATTING AREA(innings 2)
        opponent_score = 0
        print(f"{user_team} bowling and {opponant_team} is batting")
        print("it is second half ")

        for i in range(36):
            user_choice = int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if random_numbers == user_choice:
                print(f"{opponant_team} got out by {user_team} bowling ")
                if user_score>opponent_score:
                    print(f"{user_team} WON BY  DEFENDING YOUR SCORE AGAINST {opponant_team}")
                    input(f"congrat {user_team} won >>>>>>>>>")
                elif opponent_score == user_score:
                    print("it's a tie")
                else:
                    input(f"{user_team} lost<<<<<<<")
                    print(f"{opponant_team} WIN BY TAKING MORE SCORE THAN {user_team}")
                break
            else:
                opponent_score += int(random_numbers)
                print(f"{opponant_team} score {opponent_score}")
                if opponent_score > user_score:
                    input(f"{user_team} lost<<<<<<<")
                    print(f"{opponant_team} WIN BY TAKING MORE SCORE THAN {user_team}")
                    exit()
                elif opponent_score == user_score:
                    print("it's a tie")
                    continue
                else:
                    continue
                continue
#OPPONENT BATTING AREA (innings 1)
    elif random_opponent=="bat":
        input("NOTE:"
              "      GAME RULES"
              "        FOR BOWLING OR BATTING YOU SHOULD ENTER NUMBER BETWEEN 1 TO 6 ......"
              "        LET'S START  ")
        opponent_score = 0
        print(f"{user_team} bowling and {opponant_team} is batting")
        print("its a first half")

        for i in range(36):
            user_choice = int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if random_numbers == user_choice:
                print(f"{opponant_team} got out by {user_team} bowling ")
                input(f"now the first half is overr and {opponant_team} score is= {opponent_score}.. enter to continue ")
                input(f"try to get more score than {opponant_team} score by  taking more than {opponent_score}")
                break
            else:
                opponent_score += int(random_numbers)
                print(f"{opponant_team} score {opponent_score}")
                continue
        input(f"now the first half is overr and {opponant_team} score is= {opponent_score}.. enter to continue ")
        input(f"try to get more score than {opponant_team} by  taking more than {opponent_score}")
# OPPONENT BOWLING AREA (ininnges 2)
        user_score = 0
        print(f"{user_team} batting and {opponant_team} is bowling")
        print("it is second half ")

        for i in range(36):
            user_choice = int(input("enter the number  between 1 to 6...:"))
            random_numbers = random.choice(numbers)
            print(f"{opponant_team} numbers is.........:{random_numbers}")
            if user_choice == random_numbers:
                print(f"{user_team} out by putting the same number has {opponant_team}")
                if user_score>opponent_score:
                    print(f"{user_team} WON BY TAKING MORE SCORE THAN {opponant_team}")
                    input(f"congrat {user_team} won >>>>>>>>>")
                elif user_score==opponent_score:
                    print("it's a tie")
                else:
                    input(f"{user_team} lost<<<<<<<")
                    print(f"{opponant_team} WIN BY DEFENDING HIS SCORE")
                break
            else:
                user_score += int(user_choice)
                print(f"{user_team} score {user_score}")
                if user_score > opponent_score:
                    print(f"{user_team} WON BY TAKING MORE SCORE THAN {opponant_team}")
                    input(f"congrat {user_team} won >>>>>>>>>")
                    exit()
                elif user_score==opponent_score:
                    print("it's a tie")
                    continue
                else:
                    continue
                continue
    else:
        print("try to put every thing in lower case")