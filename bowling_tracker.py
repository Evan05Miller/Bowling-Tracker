#Initialize scores and series variables
all_scores = []
all_series = []

print("Welcome to the Bowling Tracker App")
print("")
print("You can insert as many games in at a time as you want")
print("")
print("Enter three consecutive games and it will become a series")
print("")
print("Type 'Info' to see all of the different commands you can do")
print("")
print("__________________________________________________________________")
print("")

def add_score( score: str ) -> list[int]:
    scores = score.split()
    new_scores = []
    valid_num = False
    if score != "DONE":
        for number in scores:
            if number.isdigit():
                valid_num = True
        if valid_num:
            if number.isdigit():
                for number in scores:
                    if int(number) <= 300 and int(number) >= 0:
                        new_scores.append(int(number))
                    else:
                        print("Please enter valid score")
                if len(new_scores) == 3:
                    if int(number) <= 300 and int(number) >= 0:
                        all_series.append(new_scores)
                    else:
                        print("Please enter valid score")
                else:
                    if int(number) <= 300 and int(number) >= 0:
                        all_scores.append(new_scores)
                    else:
                        print("Please enter a valid score")
        else:
            print("Please enter a valid score")

def avg_score( scores: list, series: list) -> str:
    count = 0
    total_score = 0
    for set in scores:
        for score in set:
            count = count + 1
            total_score = total_score + score
    for s_set in series:
        for s_score in s_set:
            count = count + 1
            total_score = total_score + s_score
    if count == 0:
        average = 0
    else:
        average = total_score // count 
    return str(average)

def avg_series( series: list) -> str:
    count = 0 
    total_score = 0 
    for set in series:
        count = count + 1
        for s_score in set:
            total_score = total_score + s_score
    if count == 0:
        average = 0
    else:
        average = total_score // count
    return str(average)

def top_score( scores: list, series: list ) -> str:
    top_score = 0 
    for set in scores:
        for score in set:
            if score > top_score:
                top_score = score
    for s_set in series:
        for s_score in s_set:
            if s_score > top_score:
                top_score = s_score
    return str(top_score)

def top_series( series: list ) -> str:
    top_series = 0
    for set in series:
        current_total = 0 
        for score in set:
            current_total = current_total + score
            if current_total > top_series:
                top_series = current_total
    return str(top_series)

def average_scores( scores: list, series: list ) -> str:
    print("Average Score: " + avg_score(scores, series))
    print("")
    print("Average Series: " + avg_series(series))

def high_scores( scores: list, series: list ) -> str:
    print("High Score: " + top_score(scores, series))
    print("")
    print("High Series: " + top_series(series))

while True:
    print("")
    user_input = input("What would you like to do?: ")
    print("")

    if user_input == "Info":
        print("Function List:")
        print("")
        print("ADD: add scores into the database")
        print("AVERAGE: view your average score over every game")
        print("CLEAR: clears all of your scores")
        print("HIGH: view your high game and series")
        print("")
        
    elif user_input == "ADD":
        score_input = input("Enter your score in either singlar form or in the form of a series seperated by spaces: ")
        add_score(score_input)
        while score_input != "DONE":
            print("")
            score_input = input("Add another score/scores or enter 'DONE' if you are finished: ")
            add_score(score_input)

    elif user_input == "AVERAGE":
        average_scores( all_scores, all_series )

    elif user_input == "CLEAR":
        all_scores = []
        all_series = []
        print("SCORES CLEARED")
    
    elif user_input == "HIGH":
        high_scores( all_scores, all_series)
    
    else:
        print("Please enter valid command")
