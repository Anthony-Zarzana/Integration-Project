"""This is a Baseball trivia game
__author__= Anthony Zarzana
"""


def print_welcome():
    """Great the user."""
    print("Welcome to my Baseball Trivia Game")
    x = input("Are you ready to play the game?")
    if x == "yes":
        print("Goodluck")
        play_game()


def play_game():
    """Play the game."""
    # This is the total amount of correct answers
    total_correct = 0
    # Amount of chances given per question
    count = 0

    question_count = 0

    print("Which team won the World Series in 1999\n")
    y = input("A: Yankees\nB: Red Sox\nC: White Sox\nD: Angles")
    while count < 1:
        if y.capitalize() == "A":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Which player had the most home runs hit in the 2018 season?\n")
    y = input("A: Nolan Arenado\nB: Mike Trout\nC: Jose Ramirez\n"
              "D: Giancarlo Stanton")
    while count < 1:
        if y.capitalize() == "B":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Who received the Manager of the Year Award in 2015?\n")
    y = input(
        "A: Brian Snitker, Atlanta Braves\nB: Torey Lovullo, Arizona D-bac"
        "ks\nC: Dave Roberts, LA Dodgers\nD: Joe Maddon, Chicago Cubs")
    while count < 1:
        if y.capitalize() == "D":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Which MLB team has the most World Series wins?\n")
    y = input("A: Atlanta Braves\nB: Arizona D-backs\nC: New York Yanke"
              "es\nD: Chicago Cubs")
    while count < 1:
        if y.capitalize() == "C":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Which pitcher was the first to throw a perfect game in the MLB?\n")
    y = input("A: Lee Richmond \nB: Jim Bunning \nC: Sandy Koufax \nD: "
              "Randy Johnson")

    while count < 1:
        if y.capitalize() == "A":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Which pitcher was the first to throw 100mph?\n")
    y = input("A: Aroldis Chapman\nB: Eddie Stanky \nC: Sandy Koufax \nD: Nol"
              ""
              "an Ryan ")
    while count < 1:
        if y.capitalize() == "D":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("How many teams are in the MLB?\n")
    y = input("A: 40 \nB: 25 \nC: 22 \nD: 30 ")
    while count < 1:
        if y.capitalize() == "D":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Who was the first major league player to hit 4 home run"
          "s in a single game?\n")
    y = input("A: Bobby Lowe \nB: Mike Trout \nC: Aaron Judge \nD: Babe Ruth ")
    while count < 1:
        if y.capitalize() == "A":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("When was the new Yankee stadium built?\n")
    y = input("A: 2010 \nB: 2009 \nC: 2008 \nD: 2005 ")
    while count < 1:
        if y.capitalize() == "B":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("When was Dodger stadium built?\n")
    y = input("A: 2002 \nB: 1956 \nC: 1962 \nD: 1963 ")
    while count < 1:
        if y.capitalize() == "C":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("When was Wrigley field built?\n")
    y = input("A: 1912 \nB: 1922 \nC: 1914 \nD: 1962 ")
    while count < 1:
        if y.capitalize() == "C":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("When was Angel Stadium of Anaheim built?\n")
    y = input("A: 2000 \nB: 1999 \nC: 1988 \nD: 1998 ")
    while count < 1:
        if y.capitalize() == "D":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Which team plays in PNC park?\n")
    y = input("A: Mets \nB: Pirates \nC: Reds \nD: Marlins ")
    while count < 1:
        if y.capitalize() == "B":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Which team plays at Tropicana Field?\n")
    y = input("A: Rays \nB: Athletics \nC: Rangers \nD: Dimondbacks ")
    while count < 1:
        if y.capitalize() == "A":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1
    count = 0

    print("Where do the Cleveland Indians play their home games?\n")
    y = input("A: Great American Ball Park \nB: Progressive Field \nC: Citi "
              "Field  "  "\nD: Busch Stadium ")
    while count < 1:
        if y.capitalize() == "B":
            count += 1
            total_correct += 1
        else:
            print("Wrong Answer")
            count += 1
        question_count += 1

    # call_the print_results_function_with_2_arguments
    print_results(total_correct, question_count)


# header for print_result function with 2 parameters
def print_results(totalcorrect, question_count):
    """Print the results."""
    print("This is the amount you got correct", str(totalcorrect) + " out of",
          question_count)


print_welcome()
