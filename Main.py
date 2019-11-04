#Anthony Zarzana
#Baseball Trivia Game
totalcorrect = 0
count = 0
def multiply(x):
    x * 3
    return x
result = multiply(2)

print("Welcome to my Baseball Trivia Game")
x = input("Are you ready to play the game?")
if x == "yes":
    print("Goodluck")
elif x == "no":
    exit(0)

print("Which team won the World Series in 1999\n")
y=input("A: Yankees\nB: Red Sox\nC: White Sox\nD: Angles")
while count < 1:
    if y == "A":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0


print("Which player had the most home runs hit in the 2018 season?\n")
y = input("A: Nolan Arenado\nB: Mike Trout\nC: Jose Ramirez\nD: Giancarlo Stanton")
while count < 1:
    if y == "B":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0

print("Who received the Manager of the Year Award in 2015?\n")
y = input("A: Brian Snitker, Atlanta Braves\nB: Torey Lovullo, Arizona D-backs\nC: Dave Roberts, LA Dodgers\nD: Joe Maddon, Chicago Cubs")
while count < 1:
    if y == "D":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0

print("Which MLB team has the most World Series wins?\n")
y = input("A: Atlanta Braves\nB: Arizona D-backs\nC: New York Yankees\nD: Chicago Cubs")
while count < 1:
    if y == "C":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0

print("Which pitcher was the first to throw a perfect game in the MLB?\n")
y = input("A: Lee Richmond \nB: Jim Bunning \nC: Sandy Koufax \nD: Randy Johnson ")
while count < 1:
    if y == "A":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0

print("Which pitcher was the first to throw a perfect game in the MLB?\n")
y = input("A: Ben Chapman \nB: Eddie Stanky \nC: Sandy Koufax \nD: Ralph Branca ")
while count < 1:
    if y == "D":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0

print("How many teams are in the MLB?\n")
y = input("A: 40 \nB: 25 \nC: 22 \nD: 30 ")
while count < 1:
    if y == "D":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0

print("Who was the first major league player to hit 4 home runs in a single game\n")
y = input("A: Bobby Lowe \nB: Mike Trout \nC: Aaron Judge \nD: Babe Ruth ")
while count < 1:
    if y == "A":
        count = 1
    else:
        print("Wrong Answer")
        count += 1

count = 0