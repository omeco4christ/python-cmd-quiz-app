# quiz.py

import random
import string

QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}

# for question, alternatives in QUESTIONS.items():
#     correct_answer = alternatives[0]

#     for alternative in random.sample(alternatives, 4):
#         print(f"  - {alternative}")

#     answer = input(f"{question}? ")
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer!r}, not {answer!r}")


for question, alternatives in QUESTIONS.items():

    # Thes correct answer is the first index
    correct_answer = alternatives[0]

    # jumble the options so that they will appear in different ordering
    sorted_alternatives = random.sample(alternatives, 4)

    # for label, alternative in zip(string.ascii_uppercase, sorted_alternatives):
    # Change the options from number to alphabet
    for label, alternative in zip(string.ascii_lowercase, sorted_alternatives):
        print(f"{label}) {alternative!r}")

    # input the users choice
    answer_label = int(input(f"{question}? "))

    # If the user chooses options that is not within the scope
    if answer_label > 3 or answer_label < 0:
        print(f"Choose any of {sorted_alternatives!r}")
    else:
        # output correct if the answer is correct
        answer = sorted_alternatives[answer_label]
        if answer == correct_answer:
            print("Correct!")
        else:
            # provide the user with the correct answer is they where wrong
            print(f"The answer is {correct_answer!r}, not {answer!r}")



# for question, alternatives in QUESTIONS.items():
#     correct_answer = alternatives[0]
#     sorted_alternatives = sorted(alternatives)
#     for label, alternative in enumerate(sorted_alternatives):
#         print(f"  {label}) {alternative}")

#     answer_label = int(input(f"{question}? "))
#     answer = sorted_alternatives[answer_label]
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer!r}, not {answer!r}")