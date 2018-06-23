# Strings for the different difficulties

easy_string = """I have a __1__ that one day this __2__ will rise up, and live out the true meaning of its creed: We hold these truths to be self-evident: that all men are created equal.
Martin Luther King jr

The greatest __3__ in living lies not in never falling, but in __4__ every time we fall.
Nelson Mandela

That is one small __5__ for a man, one giant leap for __6__.
Neil Armstrong"""

answer_list1 = ["dream", "nation", "glory", "rising", "step", "mankind" ]

medium_string = """Do not __1__ the chickens before they are __2__.

An eye for an __3__, a tooth for a __4__.

Accept that some days you are the __5__, and some days you are the __6__."""

answer_list2 = ["count", "hatched", "eye", "tooth", "pigeon", "statue"]

hard_string = """Judge your __1__ by what you had to give up in __2__ to get it.
 Dalai Lama

In the end, it is not the __3__ in your life that count. It is the __4__ in your years.
Abraham Lincoln

Be the __5__ that you wish to see in the __6__
Mahatma Gandhi"""

answer_list3 = ["success", "order", "years", "life", "change", "world"]

# Method to choose the string,which belong to the choosen difficulty

def string_to_difficulty(difficulty):
    if difficulty == "easy":
        return easy_string
    elif difficulty == "medium":
        return medium_string
    else:
        return hard_string
# Method return the right answer list to the choosen difficulty and string

def answer_list_to_difficulty(difficulty):
    if difficulty == "easy":
        return answer_list1
    elif difficulty == "medium":
        return answer_list2
    else:
        return answer_list3

# Method where the user can choose the difficulty, the method returns the difficulty.
def difficulty():
    difficult_grade = raw_input("Please enter your difficulty: easy, medium, hard:  ")
    if difficult_grade == "easy" or  difficult_grade == "medium" or difficult_grade == "hard":
        return difficult_grade
    while difficult_grade != "easy" or  difficult_grade != "medium" or difficult_grade != "hard":
        difficult_grade = raw_input("Invalid Input, please enter easy, medium or hard:  ")
        return difficult_grade

# Method to find the gaps

def find_the_gaps(number, text_with_gaps):
    number = str(number)
    for pos in text_with_gaps:
        if number in pos :
            return pos
    return None
# Method, if the answer is right, the input is the list, replacement and the right answerself.
# The method is replacing the dummy through the right answer and prints the created string and returns the listself.

def answer_is_right(quiz_string, replacement, controll_answer):
    quiz_string = " ".join(quiz_string)
    quiz_string = quiz_string.replace(replacement, controll_answer)
    print quiz_string
    quiz_string = quiz_string.split()
    return quiz_string

# Main method to play the quiz

def play_the_game(difficulty):
    quiz_string = string_to_difficulty(difficulty)
    print quiz_string
    quiz_string = quiz_string.split()
    answer_list = answer_list_to_difficulty(difficulty)
    number = 1
    countdown = 3
    for element in answer_list:
        replacement = find_the_gaps(number,quiz_string)
        if replacement != None:
            user_answer = raw_input("Please enter your answer:  ")
            if user_answer.lower() == answer_list[number -  1].lower():
                quiz_string = answer_is_right(quiz_string, replacement, answer_list[number -  1])
                number += 1
            else:
                while user_answer.lower() != answer_list[number -  1].lower() or countdown > 0:
                    user_answer = raw_input("Try again! You have " +str(countdown)+ " more tries: ")
                    countdown = countdown - 1
                    if countdown == 0:
                        return "Game Over"
                    if user_answer.lower() == answer_list[number -  1].lower():
                        quiz_string = answer_is_right(quiz_string, replacement, answer_list[number -  1])
                        number += 1
                        break
    return "You win! Quiz solved!"

print play_the_game(difficulty())
