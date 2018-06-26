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



def string_to_difficulty(difficulty):
        """
        The method gets the difficulty as a string and returns the string,
        which belongs to the choosen difficulty and return and print it.
        parameters:
            input is the difficulty as a string.
        return: Is the string which belongs to difficulty.
        """
    if difficulty == "easy":
        print easy_string
        return easy_string
    elif difficulty == "medium":
        print medium
        return medium_string
    else:
        print hard_string
        return hard_string

def answer_list_to_difficulty(difficulty):
        """
        The method gets the difficulty as string and returns the answers,
        which are strings and they are stored in a list
        parameters:
            input is the difficulty as a string
        return: the strings in a list.
        """
    if difficulty == "easy":
        return answer_list1
    elif difficulty == "medium":
        return answer_list2
    else:
        return answer_list3

def difficulty():
    """
    The method has no input, the user is asked to choose the difficulty,
    also there is a check a while loop to make sure that the user chooses a difficulty, which is available.
    parameters:
        User input which is stored as string.
    return: the difficulty as a string
    """
    difficult_grade = raw_input("Please enter your difficulty: easy, medium, hard:  ")
    if difficult_grade == "easy" or  difficult_grade == "medium" or difficult_grade == "hard":
        return difficult_grade
    while difficult_grade != "easy" or  difficult_grade != "medium" or difficult_grade != "hard":
        difficult_grade = raw_input("Invalid Input, please enter easy, medium or hard:  ")
        return difficult_grade

def find_the_gaps(number, text_with_gaps):
    """
    The method gets the number,as a int, which shows the gaps which we currently searching for.
    Also the method gets the text as a string. Then the methode is searching in the text for the number,
    which is transformed into a string, with a for loop. And if the number is found, the part of the text is returned.
    parameters:
        input is a number as int and the text as a string.
    return: None, when the number isn't found or the part of the text with the number in it as a string.
    """
    number = str(number)
    for pos in text_with_gaps:
        if number in pos :
            return pos
    return None

def answer_is_right(quiz_string, replacement, controll_answer):
    """
    The method  gets three inputs: the text as List with strings in it, replacement,
    which is a string and the right answer as string.
    First the text is transformed into a string and after that the replacement is replaced through the right answer.
    After that the the new text is printed.
    The next is to transform the string into a list again and return it.
    parameters:
        quiz string as list filled with strings, replacement is a string and the controll answer is a string,too.
    return: text with the right answer in it as list.
    """
    quiz_string = " ".join(quiz_string)
    quiz_string = quiz_string.replace(replacement, controll_answer)
    print quiz_string
    quiz_string = quiz_string.split()
    return quiz_string

def play_the_game(difficulty):
    """
    The input for this method is the difficulty as a string. First the answer and the text as a string,
    which are belonging to the difficulty is defined to the methods string_to_difficulty and answer_list_to_difficulty.
    After that, there is a for loop which is going through the answer list to make sure every gap is filled.
    In the next step the the method find_the_gaps is used to find the gap which belongs to the actual number.
    Then the user has to fill in the first gap. if the answer is wrong, a while starts until the user entered the right answer or the countdown has reached 0.
    The method answer_is_right starts then. When every gap is filled the method returns a string.
    parameters:
        input is difficulty as string, in the method number as a int is used to show on which gap is searched for at the moment
    return: string when the quiz is solved or the countdown has reached 0.
    """
    quiz_string = string_to_difficulty(difficulty)
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
