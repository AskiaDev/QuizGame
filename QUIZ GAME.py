# first we create a functions new_game, check_answer, display_score and play_again
def new_game():
    # so lets create a variable name guesses and assign it to an empty list
    guesses = []
    # we will declared a variable called correct guesses and assign it to 0
    correct_guesses = 0
    # we will set of question_num set it equal to 1 to represent the first question
    question_num = 1
    # so we'll need to display all of our question within our dictionary using a for loop
    for key in questions:
        print("------------------------------")
        # we'll print the key in our dictionary to check if its working. the key in dictionary is all of the questions.
        print (key)
        # so will need to display all of the different options within our 2d lists using for loop
        for i in options[question_num-1]: # we will set an index for options. note: the index is going to be our question number minus 1, we initialize the question as some sort of counter since we initally assign it to 1 we were just going to subtract to 1 to become 0 as the index
            print(i)
        # lets go for user input. lets set a variable name to guess
        guess = input("Enter (A, B, or C) : ")
        # we will use upper method to prevent case sensitive
        guess = guess.upper()
        # after the end of the game will compare the guesses and correct answer and display it, we will append our current guess to our list (guesses)
        guesses.append(guess)
        # so next lets check if the user is correct answer, to do that we are going to call the check_answer function, we will pass in the key for the current question that were on, so lets assign the point we may or may not receive to our variable of correct guesses which is initially zero(correct_guesses = 0) the check_answer will return 1 point if the user has get a point and zero if it doesnt (+=)
        correct_guesses += check_answer(questions.get(key), guess)
        # lets increment question_num by 1 (+=)
        question_num += 1
        # so we'll need to display only the first list for the first question
    #so now we will call the function (display_score) note: make sure you do not write it inside the for loop it should be outside of the for loop, after we answer all of our question we will display our score, we will pass the arguments (correct_guesses, guesses)
    display_score(correct_guesses, guesses)
def check_answer(answer, guess):
    # we will check the answer if is equal to our guess
    if answer == guess:
        print("FANTASTIC!")
        return 1 # so this is returning value we should assign this
    else:
        print("UH - OH YOU ARE WRONG")
        return 0 # you dont have get a point
# we need to pass in the arguments (correct_guesses, guesses)
def display_score(correct_guesses, guesses):
    print("------------------------------")
    # we'll print the results
    print("          RESULTS              ")
    print("------------------------------")
    # we'll print also our answers, reminders: use end=""
    print("Answers: ", end="")
    #we will display our values within our dictionary using for loop
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    # in this for loop we will display all of our guesses in guesses list
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your final score is: " + str(score) + "%")
def play_again():
    # lets set a variable response assign it to input prompt
    response = input("Do you want to play again? (yes/no): ")
    response = response.lower()

    if response == "yes":
        return True
    else:
        return False
# second lets create a dictionary that has a key value pairs, the key is the questions and the value is the correct answers.
questions = {
        "Who invented the computer" : "B",
        "What CPU stands for?" : "A",
        "What GPU stands for?" : "C",
        "What is the first OS" : "B"
}
# second lets create a 2d lists that has all the choices A,B,C,D. each list corresponds to a key value pair within the dict.
options = [
    ["A. Elon Musk", "B. Charles Babbage", "C. Mark Zuckerburg"],
    ["A. Central Processing Unit", "B. Central Processing and Utility", "Central Processing and Unification"],
    ["A. General Purpose Unit", "B. Graphics Processing and Utility", "C. Graphics Processing Unit"],
    ["A. Windows", "B. GM-NAA I/O", "C. MAC OS"]
]

# lets call the new game() function if we call this it will generate our dictionary that contains of questions and our 2d list different options in each questions.
new_game()
while play_again():
    new_game()

print("THANK YOU FOR USING MY PROGRAM")
print("AskiaDev")