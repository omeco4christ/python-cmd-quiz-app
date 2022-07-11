# How to Build a Command Line Quiz App Using Python

This is a command line Quiz application built with Python.

In this tutorial, you will build a trivia app using python. This step-by-step guide, you will learn:

- Interact with the user in the terminal
- Improve the usability of your application
- Refactor your application to continuously improve it
- Store data in dedicated data files

## Table of Content
1. Introduction
2. Project Overview
3. Prerequisites
4. Step 1: Ask Questions
5. Step 2: Make Your Application User-Friendly
6. Step 3: Organize Your Code With Functions
7. Step 4: Separate Data Into Its Own File
8. Step 5: Expand Your Quiz Functionality
9. Step 6: Support Several Quiz Topics
10. Conclusion

### Introduction

This is how the quiz app will work. You first choose a topic for your questions. Then, for each question, you’ll choose an answer from a set of alternatives. Some questions may have multiple correct answers. You can access a hint to help you along the way. After answering a question, you’ll read an explanation that can provide more context for the answer.


### Project Overview

You’ll start by creating a basic Python quiz application that’s only capable of asking a question, collecting an answer, and checking whether the answer is correct. From there, you’ll add more and more features in order to make your app more interesting, user-friendly, and fun.

You’ll build the quiz application iteratively by going through the following steps:

- Create a basic application that can ask multiple-choice questions.
- Make the app more user-friendly by improving how it looks and how it handles user errors.
- Refactor the code to use functions.
- Separate question data from source code by storing questions in a dedicated data file.
- Expand the app to handle multiple correct answers, give hints, and provide explanations.
- Add interest by supporting different quiz topics to choose from.

As you follow along, you’ll gain experience in starting with a small script and expanding it. This is an important skill in and of itself. Your favorite program, app, or game probably started as a small proof of concept that later grew into what it is today.


### Prerequisites

In this project, you’ll build a quiz application using Python’s basic building blocks. While working through the steps, it’s helpful if you’re comfortable with the following concepts:

- Reading input from the user at the terminal
- Organizing data in structures like lists, tuples, and dictionaries
- Using if statements to check different conditions
- Repeating actions with for and while loops
- Encapsulating code with functions

If you’re not confident in your knowledge of these prerequisites, then that’s okay too! In fact, going through this project will help you practice these concepts.

### Step 1: Ask Questions

In this step, you’ll learn how to create a program that can ask questions and check answers. This will be the foundation of your quiz application, which you’ll improve upon in the rest of the project.

Your program will be able to ask questions and check answers. This version includes the basic functionality that you need, but you’ll add more functionality in later steps. 

> Get User Information With input()

One of Python’s built-in functions is input(). You can use it to get information from the user. For a first example, run the following in your terminal

```
for windows: python

for linux: python3

```

We shall be using linux for this project. 

next, the python shell will come up in the terminal.

run the below code

```
>>> name = input("What's your name? ")
What's your name? John Deo

>>> name
'John Deo'

```

Note: remember to always close the python shell using

```
>>> quit()

```


input() takes an optional prompt that’s displayed to the user before the user enters information. In the example above, the prompt is shown in the highlighted line, and the user enters John Deo before hitting Enter. Whatever the user enters is returned from input(). This is seen in the REPL example, as the string 'John Deo' has been assigned to name.

You can use input() to have Python ask you questions and check your answers. Try the following:

```
>>> answer = input("When was the first known use of the word 'quiz'? ")
When was the first known use of the word 'quiz'? 1781

>>> answer == 1781
False

>>> answer == "1781"
True

```
The above example shows one thing that you need to be aware of: input() always returns a text string, even if that string contains only digits. As you’ll soon see, this won’t be an issue for the our quiz project. 

However, if you wanted to use the result of input() for mathematical calculations, then you’d need to convert it first.

Lets start building your quiz application. Open your code editor and create the file quiz.py with the following content:

```
# quiz.py

answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct!")
else:
    print(f"The answer is '1781', not {answer!r}")

```

The bove code is very similar to what you experimented with in the python shell. 

You can run your application to test the project:

```
$ python3 quiz.py

When was the first known use of the word 'quiz'? 1871
The answer is '1781', not '1871'

```

If you happen to give the wrong answer, then you’ll be gently corrected so that you’ll hopefully do better next time.

A quiz with only one question isn’t very exciting! You can ask another question by repeating your code. Modify your code in quiz.py to look like the code below.

```

# quiz.py

answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct!")
else:
    print(f"The answer is '1781', not {answer!r}")

answer = input("Which built-in function can get information from the user? ")
if answer == "input":
    print("Correct!")
else:
    print(f"The answer is 'input', not {answer!r}")

```

You’ve added a question by copying and pasting the previous code then changing the question text and the correct answer. Again, you can test this by running the script:

```
$ python3 quiz.py

When was the first known use of the word 'quiz'? 1781
Correct!
Which built-in function can get information from the user? get
The answer is 'input', not 'get'

```

It works! However, copying and pasting code like this isn’t great. There’s a programming principle called Don’t Repeat Yourself (DRY), which says that you should usually avoid repeated code because it gets hard to maintain.

Next, you’ll start improving your code to make it easier to work with.


> Use Lists and Tuples to Avoid Repetitive Code


Python provides several flexible and powerful data structures. You can usually replace repeated code with a tuple, a list, or a dictionary in combination with a for loop or a while loop.

Instead of repeating code, you’ll treat your questions and answers as data and move them into a data structure that your code can loop over. The immediate—and often challenging—question then becomes how you should structure your data.

There’s never one uniquely perfect data structure. You’ll usually choose between several alternatives. Throughout this project, you’ll revisit your choice of data structure several times as your application grows.

For now, choose a fairly simple data structure:

A list will hold several question elements.
Each question element will be a two-tuple consisting of the question text and the answer.
You can then store your questions as follows:

```
[
    ("When was the first known use of the word 'quiz'", "1781"),
    ("Which built-in function can get information from the user", "input"),
]

```
This fits nicely with how you want to use your data. You’ll loop over each question, and for each question, you want access to both the question and answer.

Change your quiz.py file so that you store your questions and answers in the QUESTIONS data structure:

```
# quiz.py

QUESTIONS = [
    ("When was the first known use of the word 'quiz'", "1781"),
    ("Which built-in function can get information from the user", "input"),
    ("Which keyword do you use to loop over a given list of elements", "for")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

```
When you run this code, it shouldn’t look any different from how it did earlier. In fact, you haven’t added any new functionality. Instead, you’ve refactored your code so that it’ll be easier to add more questions to your application.

In the previous version of your code, you needed to add five new lines of code for each question that you added. Now, the for loop takes care of running those five lines for each question. To add a new question, you only need to add one line spelling out the question and the corresponding answer.

Next, you’ll make your quiz application easier to use by adding answer alternatives for each question.

> Provide Multiple Choices

Using input() is a great way to read input from your user. However, the way you’re currently using it can end up being frustrating. For example, someone may answer one of your questions like this:

```

Which built-in function can get information from the user? input()
The answer is 'input', not 'input()'

```

Should they will really be marked wrong because they included the parentheses to indicate that the function is callable? You can take away a lot of guesswork for the users by giving them alternatives. For example:

```
- get
  - input
  - print
  - write
Which built-in function can get information from the user? input
Correct!

```

Here, the alternatives show that you expect the answer to be entered without parentheses. In the example, the alternatives are listed before the question. This is a bit counterintuitive, but it’s easier to implement into your current code. You’ll improve this in the next step.

In order to implement answer alternatives, you need your data structure to be able to record three pieces of information for each question:

* The question text
* The correct answer
* Answer alternatives


It’s time to revisit QUESTIONS for the first—but not the last—time and make some changes to it. It makes sense to store the answer alternatives in a list, as there can be any number of them and you just want to display them to the screen. Furthermore, you can treat the correct answer as one of the answer alternatives and include it in the list, as long as you’re able to retrieve it later.

You decide to change QUESTIONS to a dictionary where the keys are your questions and the values are the lists of answer alternatives. You consistently put the correct answer as the first item in the list of alternatives so that you can identify it.

Note: You could continue to use a list of two-tuples to hold your questions. In fact, you’re only iterating over the questions and answers, not looking up the answers by using a question as a key. Therefore, you could argue that the list of tuples is a better data structure for your use case than a dictionary.

However, you use a dictionary because it looks better visually in your code, and the roles of questions and answer alternatives are more distinct.

You update your code to loop over each item in your newly minted dictionary. For each question, you pick out the correct answer from the alternatives, and you print out all the alternatives before asking the question:

```

# quiz.py

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

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

```

If you always showed the correct answer as the first alternative, then your users would soon catch on and be able to guess the correct answer every time. Instead, you change the order of the alternatives by sorting them using the sorted() function. 

> Syntax of sorted()

```
sorted(iterable, key=None, reverse=False)

```
> sorted() Parameters

The sorted() function takes a maximum of three paramenters:

* iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.

* reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.

* key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

> sorted() Return Value

The sorted() function returns a sorted list.

> item()

On the other hand, The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

The view object will reflect any changes done to the dictionary, see example below.

```
dictionary.items()

```

Test your application:

```
$ python3 quiz.py
  - 1771
  - 1781
  - 1871
  - 1881
When was the first known use of the word 'quiz'? 1781
Correct!

...

  - To combine several strings into one
  - To compress several files into one archive
  - To get information from the user
  - To iterate over two or more sequences at the same time
What's the purpose of the built-in zip() function?
    To itertate over two or more sequences at the same time
The answer is 'To iterate over two or more sequences at the same time',
    not 'To itertate over two or more sequences at the same time'
```


The last question reveals another experience that can be frustrating for the user. In this example, they’ve chosen the correct alternative. However, as they were typing it, a typo snuck in. Can you make your application more forgiving?

You know that the user will answer with one of the alternatives, so you just need a way for them to communicate which alternative they choose. You can add a label to each alternative and only ask the user to enter the label.

Update the application to use enumerate() to print the index of each answer alternative:

```

# quiz.py

QUESTIONS = {
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

```

> enumerate()

The enumerate() method adds a counter to an iterable and returns it (the enumerate object).


You store the reordered alternatives as sorted_alternatives so that you can look up the full answer based on the answer label that the user enters. Recall that input() always returns a string, so you need to convert it to an integer using the int() function before you treat it as a list index.

> int()

The int() method converts any string, bytes-like object or a number to integer and returns.

Now, it’s more convenient to answer the questions:

```

$ python quiz.py
  0) each
  1) for
  2) loop
  3) while
Which keyword do you use to loop over a given list of elements? 2
The answer is 'for', not 'loop'
  0) To combine several strings into one
  1) To compress several files into one archive
  2) To get information from the user
  3) To iterate over two or more sequences at the same time
What's the purpose of the built-in zip() function? 3
Correct!
  0) Bubble sort
  1) Merge sort
  2) Quicksort
  3) Timsort
What's the name of Python's sorting algorithm? 3
Correct!

```

### Step 2: Make Your Application User-Friendly

In this second step, you’ll improve on your quiz application to make it easier to use. In particular, you’ll improve the following:

- How the application looks and feels
- How you summarize the user’s results
- What happens if your user enters a nonexistent alternative
- Which order you present the questions and alternatives in

Looking back at how your quiz application is currently presented. It’s not very attractive. There are no blank lines that tell you where a new question starts, and the alternatives are listed above the question, which is a bit confusing. Furthermore, the numbering of the different choices start at 0 instead of 1, which would be more natural.

In your next update to quiz.py, you’ll number the questions themselves and present the question text above the answer alternatives. Additionally, you’ll use lowercase letters instead of numbers to identify answers:

```

# quiz.py

from string import ascii_lowercase

QUESTIONS = {
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ]
}

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

```

You use string.ascii_lowercase to get letters that label your answer alternatives. You combine letters and alternatives with zip() and store them in a dictionary as follows:

```

>>> import string
>>> dict(zip(string.ascii_lowercase, ["1771", "1781", "1871", "1881"]))
{'a': '1771', 'b': '1781', 'c': '1871', 'd': '1881'}

```

You use these labeled alternatives when you display the options to the user and when you look up the user’s answer based on the label that they entered. Note the use of the special escape string "\n". This is interpreted as a newline and adds a blank line on the screen. This is a simple way to add some organization to your output:

```

$ python quiz.py

Question 1:
What's the purpose of the built-in zip() function?
  a) To combine several strings into one
  b) To compress several files into one archive
  c) To get information from the user
  d) To iterate over two or more sequences at the same time

Choice? d
⭐ Correct! ⭐

Question 2:
What's the name of Python's sorting algorithm?
  a) Bubble sort
  b) Merge sort
  c) Quicksort
  d) Timsort

Choice? c
The answer is 'Timsort', not 'Quicksort'

```

Your output is still mostly monochrome in the terminal, but it’s more visually pleasing, and it’s easier to read.

> Keep Score

Now that you’re numbering the questions, it would also be nice to keep track of how many questions the user answers correctly. You can add a variable, num_correct, to take care of this:


```

# quiz.py

from string import ascii_lowercase

QUESTIONS = {
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],
}

num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")


```

You increase num_correct for each correct answer. The num loop variable already counts the total number of questions, so you can use that to report the user’s result.

> Handle User Errors

So far, you haven’t worried too much about what happens if the user enters an answer that’s not valid. In the different versions of your app, this oversight could result in the program raising an error or—less dramatically—registering a user’s invalid answer as wrong.

You can handle user errors in a better way by allowing the user to re-enter their answer when they enter something invalid. One way to do this is to wrap input() in a while loop:

```

>>> while (text := input()) != "quit":
...     print(f"Echo: {text}")
...
Hello!
Echo: Hello!
Walrus ...
Echo: Walrus ...
quit

```

The condition (text := input()) != "quit" does a few things at once. It uses an assigment expression (:=), often called the walrus operator, to store the user input as text and compare it to the string "quit". The while loop will run until you type quit at the prompt.

In your quiz application, you use a similar construct to loop until the user gives a valid answer:

```

# quiz.py

from string import ascii_lowercase

QUESTIONS = {
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
}

num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")

```
If you enter an invalid choice at the prompt, then you’ll be reminded about your valid choices:

```

$ python quiz.py

Question 1:
How do you iterate over both indices and elements in an iterable?
  a) enumerate(iterable)
  b) enumerate(iterable, start=1)
  c) range(iterable)
  d) range(iterable, start=1)

Choice? e
Please answer one of a, b, c, d

Choice? a
⭐ Correct! ⭐

```

Note that once the while loops exits, you’re guaranteed that answer_label is one of the keys in labeled_alternatives, so it’s safe to look up answer directly. Next, you’ll add one more improvement by injecting some randomness into your quiz.

> Add Variety to Your Quiz

Currently, when you run your quiz application, you’re always asking the questions in the same order as they’re listed in your source code. Additionally, the answer alternatives for a given question also come in a fixed order that never changes.

You can add some variety to your quiz by changing things up a little. You can randomize both the order of the questions and the order of the answer alternatives for each question:


```

# quiz.py

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")

```

You use random.sample() to randomize the order of your questions and the order of the answer alternatives. Usually, random.sample() picks out a few random samples from a collection. However, if you ask for as many samples as there are items in the sequence, then you’re effectively randomly reordering the whole sequence:

```

>>> import random
>>> random.sample(["one", "two", "three"], k=3)
['two', 'three', 'one']

```

Additionally, you cap the number of questions in the quiz to NUM_QUESTIONS_PER_QUIZ which is initially set to five. If you include more than five questions in your application, then this also adds some variety as to which questions get asked in addition to the order in which they’re asked.

* Note: You can also use random.shuffle() to shuffle your questions and alternatives. The difference is that shuffle() reorders sequences in place, which means that it changes your underlying QUESTIONS data structure. sample() creates new lists of questions and alternatives, instead.

In your current code, using shuffle() wouldn’t be a problem because QUESTIONS is reset every time you run your quiz application. It could become a problem down the line, for example if you implement the possibility of asking the same question several times. Your code is usually simpler to reason about if you don’t change or mutate your underlying data structure.

Throughout this step, you’ve improved on your quiz application. It’s now time to take a step back and consider the code itself. In the next section, you’ll reorganize the code so that you keep it modular and ready for further development.


### Step 3: Organize Your Code With Functions

In this step, you’ll refactor your code. Refactoring means that you’ll change your code, but your application’s behavior and your user’s experience will stay as they are. This may not sound very exciting, but it’ll be tremendously useful down the line, as good refactorings make it more convenient to maintain and expand your code.

Currently, your code isn’t particularly organized. All your statements are fairly low level. You’ll define functions to improve your code. A few of their advantages are the following:

- Functions name higher-level operations that can help you get an overview of your code.
- Functions can be reused.

> Prepare Data

Many games and applications follow a common life cycle:

- Preprocess: Prepare initial data.
- Process: Run main loop.
- Postprocess: Clean up and close application.

In your quiz application, you first read the available questions, then you ask each of the questions, before finally reporting the final score. If you look back at your current code, then you’ll see these three steps in the code. But the organization is still a bit hidden within all the details.

You can make the main functionality clearer by encapsulating it in a function. You don’t need to update your quiz.py file yet, but note that you can translate the previous paragraph into code that looks like this:

```
def run_quiz():
    # Preprocess
    questions = prepare_questions()

    # Process (main loop)
    num_correct = 0
    for question in questions:
        num_correct += ask_question(question)

    # Postprocess
    print(f"\nYou got {num_correct} correct")

```


This code won’t run as it is. The functions prepare_questions() and ask_question() haven’t been defined, and there are some other details missing. Still, run_quiz() encapsulates the functionality of your application at a high level.

Writing down your application flow at a high level like this can be a great start to uncover which functions are natural building blocks in your code. In the rest of this section, you’ll fill in the missing details:

Implement prepare_questions().
Implement ask_question().
Revisit run_quiz().
You’re now going to make quite substantial changes to the code of your quiz application as you’re refactoring it to use functions. Before doing so, it’s a good idea to make sure you can revert to the current state, which you know works. You can do this either by saving a copy of your code with a different filename or by making a commit if you’re using a version control system.

Once you’ve safely stored your current code, start with a new quiz.py that only contains your imports and global variables. You can copy these from your previous version:

```

# quiz.py

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ]
}

```

Remember that you’re only reorganizing your code. You’re not adding new functionality, so you won’t need to import any new libraries.

Next, you’ll implement the necessary preprocessing. In this case, this means that you’ll prepare the QUESTIONS data structure so that it’s ready to be used in your main loop. For now, you’ll potentially limit the number of questions and make sure they’re listed in a random order:

```

# quiz.py

# ...

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

```
Note that prepare_questions() deals with general questions and num_questions parameters. Afterward, you’ll pass in your specific QUESTIONS and NUM_QUESTIONS_PER_QUIZ as arguments. This means that prepare_questions() doesn’t depend on your global variables. With this decoupling, your function is more general, and you can later more readily replace the source of your questions.

> Ask Questions

Look back on your sketch for the run_quiz() function and remember that it contains your main loop. For each question, you’ll call ask_question(). Your next task is to implement that helper function.

Think about what ask_question() needs to do:

1. Pick out the correct answer from the list of alternatives
2. Shuffle the alternatives
3. Print the question to the screen
4. Print all alternatives to the screen
5. Get the answer from the user
6. Check that the user’s answer is valid
7. Check whether the user answered correctly or not
8. Add 1 to the count of correct answers if the answer is correct

These are a lot of small things to do in one function, and you could consider whether there’s potential for further modularization. For example, items 3 to 6 in the list above are all about interacting with the user, and you can pull them into yet another helper function.

To achieve this modularization, add the following get_answer() helper function to your source code:

```

# quiz.py

# ...

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

```

This function accepts a question text and a list of alternatives. You then use the same techniques as earlier to label the alternatives and ask the user to enter a valid label. Finally, you return the user’s answer.

Using get_answer() simplifies your implementation of ask_question(), as you no longer need to handle the user interaction. You can do something like the following:

```
# quiz.py

# ...

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

```

You first randomly reorder the answer alternatives using random.shuffle(), as you did earlier. Next, you call get_answer(), which handles all details about getting an answer from the user. You can therefore finish up ask_question() by checking the correctness of the answer. Observe that you return 1 or 0, which indicates to the calling function whether the answer was correct or not.

You’re now ready to implement run_quiz() properly. One thing you’ve learned while implementing prepare_questions() and ask_question() is which arguments you need to pass on:

```
# quiz.py

# ...

def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")

```

As earlier, you use enumerate() to keep a counter that numbers the questions you ask. You can increment num_correct based on the return value of ask_question(). Observe that run_quiz() is your only function that directly interacts with QUESTIONS and NUM_QUESTIONS_PER_QUIZ.

Your refactoring is now complete, except for one thing. If you run quiz.py now, then it’ll seem like nothing happens. In fact, Python will read your global variables and define your functions. However, you’re not calling any of those functions. You therefore need to add a function call that starts your application:

```

# quiz.py

# ...

if __name__ == "__main__":
    run_quiz()

```

You call run_quiz() at the end of quiz.py, outside of any function. It’s good practice to protect such a call to your main function with an if __name__ == "__main__" test. This special incantation is a Python convention that means that run_quiz() is called when you run quiz.py as a script, but it’s not called when you import quiz as a module.

That’s it! You’ve refactored your code into several functions. This will help you in keeping track of the functionality of your application. It’ll also be useful in this tutorial, as you can consider changes to individual functions instead of changing the whole script.

Below is the full code:

```
# quiz.py

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881",
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write",
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop",
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort",
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ]
}

def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

if __name__ == "__main__":
    run_quiz()

```

Through this step, you’ve refactored your code to make it more convenient to work with. You separated your commands into well-organized functions that you can continue to develop. In the next step, you’ll take advantage of this by improving how you read questions into your application.


### Step 4: Separate Data Into Its Own File

You’ll continue your refactoring journey in this step. Your focus will now be how you provide questions to your application.

So far, you’ve stored the questions directly in your source code in the QUESTIONS data structure. It’s usually better to separate your data from your code. This separation can make your code more readable, but more importantly, you can take advantage of systems designed for handling data if it’s not hidden inside your code.

In this section, you’ll learn how to store your questions in a separate data file formatted according to the TOML standard. Other options—that you won’t cover in this tutorial—are storing the questions in a different file format like JSON or YAML, or storing them in a database, either a traditional relational one or a NoSQL database.

> Move Questions to a TOML File

TOML is branded as “a config file format for humans” (Source). It’s designed to be readable by humans and uncomplicated to parse by computers. Information is represented in key-value pairs that can be mapped to a hash table data structure, like a Python dictionary.

TOML supports several data types, including strings, integers, floating-point numbers, Booleans, and dates. Additionally, data can be structured in arrays and tables, which are similar to Python’s lists and dictionaries, respectively. TOML has been gaining popularity over the last years, and the format is stable after version 1.0.0 of the format specification was released in January 2021.

Create a new text file that you’ll call questions.toml, and add the following content:

```
# questions.toml

"When does __name__ == '__main__' equal True in a Python file" = [
    "When the file is run as a script",
    "When the file is imported as a module",
    "When the file has a valid name",
    "When the file only has one function",
]

"Which version of Python is the first with TOML support built in" = [
    "3.11", "3.9", "3.10", "3.12"
]

```

While there are differences between TOML syntax and Python syntax, you’ll recognize elements like using quotation marks (") for text and square brackets ([]) for lists of elements.

To work with TOML files in Python, you need a library that parses them. In this tutorial, you’ll use tomli. This will be the only package you use in this project that’s not part of Python’s standard library.

* Note: TOML support is added to Python’s standard library in Python 3.11. If you’re already using Python 3.11, then you can skip the instructions below to create a virtual environment and install tomli. Instead, you can immediately start coding by replacing any mentions of tomli in your code with the compatible tomllib.

Later in this section, you’ll learn how to write code that can use tomllib if it’s available and fall back to tomli if necessary.

Before installing tomli, you should create and activate a virtual environment:

```
Windows: 

PS> python -m venv venv
PS> venv\Scripts\Activate.ps1

You can then install tomli with pip:

(venv) PS> python -m pip install tomli


-------------------------------------------------------

Linux: 

$ python -m venv venv
$ source venv/bin/activate

You can then install tomli with pip:

(venv) $ python -m pip install tomli

```

You can check that you have tomli available by parsing questions.toml, which you created earlier. Open up your Python Shell and test the following code:

```
>>> import tomli
>>> with open("questions.toml", mode="rb") as toml_file:
...     questions = tomli.load(toml_file)
...

>>> questions
{"When does __name__ == '__main__' equal True in a Python file":
    ['When the file is run as a script',
     'When the file is imported as a module',
     'When the file has a valid name',
     'When the file only has one function'],
 'Which version of Python is the first with TOML support built-in':
    ['3.11', '3.9', '3.10', '3.12']}

```

First, observe that questions is a regular Python dictionary that has the same form as your QUESTIONS data structure that you’ve been using so far.

You can use tomli to parse TOML information in two different ways. In the example above, you use tomli.load() to read TOML from an open file handle. Alternatively, you could use tomli.loads() to read TOML from a text string.

* Note: You need to open files in binary mode by using mode="rb" before passing them to tomli.load(). This is so that tomli can make sure that the UTF-8 encoding of the TOML file is correctly handled.

If you use tomli.loads(), then the string you pass in will be interpreted as UTF-8.

You can integrate the TOML file into your quiz application by updating the preamble of your code, where you do your imports and define the global variables:

```

# quiz.py

# ...

import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())

# ...

```

Instead of doing a plain import tomli like you did earlier, you wrap your import in a try … except statement that first tries to import tomllib. If that fails, then you import tomli but rename it to tomllib. The effect of this is that you’ll use the Python 3.11 tomllib if it’s available and fall back to tomli if it’s not.

You’re using pathlib to handle the path to questions.toml. Instead of hard-coding the path to questions.toml you rely on the special __file__ variable. In practice, you’re stating that it’s located in the same directory as your quiz.py file.

Finally, you use read_text() to read the TOML file as a text string and then loads() to parse that string into a dictionary. As you saw in the previous example, loading the TOML file results in the same data structure as you previously had for your questions. Once you’ve made the changes to quiz.py, your quiz application should still function the same, although the questions are defined in the TOML file instead of in your source code.

Go ahead and add a few more questions to your TOML file to confirm that it’s being used

> Add Flexibility to Your Data Format

You’ve moved your question data out of your source code and into a dedicated data file format. One advantage of TOML over a regular Python dictionary is that you can add some more structure to your data while keeping it fairly readable and maintainable.

One notable feature of TOML is tables. These are named sections that map to nested dictionaries in Python. Furthermore, you can use arrays of tables, which are represented by lists of dictionaries in Python.

You can take advantage of these to be more explicit when defining your questions. Consider the following TOML snippet:

```

[[questions]]
question = "Which version of Python is the first with TOML support built in"
answer = "3.11"
alternatives = ["3.9", "3.10", "3.12"]

```

Regular tables start with a single-bracketed line like [questions]. You indicate an array of tables by using double brackets, like above. You can parse the TOML with tomli:

```

>>> toml = """
... [[questions]]
... question = "Which version of Python is the first with TOML support built in"
... answer = "3.11"
... alternatives = ["3.9", "3.10", "3.12"]
... """

>>> import tomli
>>> tomli.loads(toml)
{'questions': [
  {
    'question': 'Which version of Python is the first with TOML support built in',
    'answer': '3.11',
    'alternatives': ['3.9', '3.10', '3.12']
  }
]}

```

This results in a nested data structure, with an outer dictionary in which the questions key points to a list of dictionaries. The inner dictionaries have the question, answer, and alternatives keys.

This structure is a bit more complicated than what you’ve used so far. However, it’s also more explicit, and you don’t need to rely on conventions such as the first answer alternative representing the correct answer.

You’ll now convert your quiz application so that it takes advantage of this new data structure for your questions. First, reformat your questions in questions.toml. You should format them as follows:

```

# questions.toml

[[questions]]
question = "Which version of Python is the first with TOML support built in"
answer = "3.11"
alternatives = ["3.9", "3.10", "3.12"]

[[questions]]
question = "What's the name of the list-like data structure in TOML"
answer = "Array"
alternatives = ["List", "Sequence", "Set"]

```

Each question is stored inside an individual questions table with key-value pairs for the question text, the correct answer, and the answer alternatives.

Principally, you’ll need to make two changes to your application source code to use the new format:

Read questions from the inner questions list.
Use the inner question dictionaries when asking questions.
These changes touch on your main data structure, so they require several small code changes throughout your code.

First, change how you read the questions from the TOML file:

```
# quiz.py

# ...

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

```

You change prepare_questions() to do the reading of the TOML file and pick out the questions list. Additionally, you can simplify the main loop in run_quiz() since all information about a question is contained in a dictionary. You don’t keep track of the question text and alternatives separately.

This latter point requires some changes in ask_question() as well:

```

# quiz.py

# ...

def ask_question(question):
    correct_answer = question["answer"]
    alternatives = [question["answer"]] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question["question"], ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

```

You now pick out the question text, the correct answer, and the answer alternatives explicitly from the new question dictionary. One nice thing with this is that it’s more readable than the earlier convention of assuming the first answer alternative to be the correct answer.

You don’t need to make any changes in get_answer(), because that function already dealt with question text and lists of alternatives in general. That hasn’t changed.

Below if the question.toml full code:

```

# questions.toml

[[questions]]
question = "When was the first known use of the word 'quiz'"
answer = "1781"
alternatives = ["1771", "1871", "1881"]

[[questions]]
question = "Which built-in function can get information from the user"
answer = "input"
alternatives = ["get", "print", "write"]

[[questions]]
question = "What's the purpose of the built-in zip() function"
answer = "To iterate over two or more sequences at the same time"
alternatives = [
    "To combine several strings into one",
    "To compress several files into one archive",
    "To get information from the user",
]

[[questions]]
question = "What does dict.get(key) return if key isn't found in dict"
answer = "None"
alternatives = ["key", "True", "False"]

[[questions]]
question = "How do you iterate over both indices and elements in an iterable"
answer = "enumerate(iterable)"
alternatives = [
    "enumerate(iterable, start=1)",
    "range(iterable)",
    "range(iterable, start=1)",
]

[[questions]]
question = "What's the official name of the := operator"
answer = "Assignment expression"
alternatives = ["Named expression", "Walrus operator", "Colon equals operator"]

[[questions]]
question = "What's one effect of calling random.seed(42)"
answer = "The random numbers are reproducible."
alternatives = [
    "The random numbers are more random.",
    "The computer clock is reset.",
    "The first random number is always 42.",
]

[[questions]]
question = "When does __name__ == '__main__' equal True in a Python file"
answer = "When the file is run as a script"
alternatives = [
    "When the file is imported as a module",
    "When the file has a valid name",
    "When the file only has one function",
]

[[questions]]
question = "Which version of Python is the first with TOML support built in"
answer = "3.11"
alternatives = ["3.9", "3.10", "3.12"]

[[questions]]
question = "What's the name of the list-like data structure in TOML"
answer = "Array"
alternatives = ["List", "Sequence", "Set"]

```


Below is quiz.py full code:

```
# quiz.py

import pathlib
import random
from string import ascii_lowercase
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def ask_question(question):
    correct_answer = question["answer"]
    alternatives = [question["answer"]] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question["question"], ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

if __name__ == "__main__":
    run_quiz()

```

Your new flexible format for defining questions gives you some options in adding more functionality to your quiz application. You’ll dive into some of these in the next step.


### Step 5: Expand Your Quiz Functionality

In this fifth step, you’ll add more functionality to your quiz application. Finally, the refactoring you’ve done in the previous steps will pay off! You’ll add the following features:

1. Questions with multiple correct answers
2. Hints that can point toward the correct answer
3. Explanations that can act as teaching moments

These new features provide a more interesting experience to anyone challenging themselves through your quiz application. 

> Allow Multiple Correct Answers

Some questions may have multiple correct answers, and it’ll be great if your quiz can handle those as well. In this section, you’ll add support for multiple correct answers.

First, you need to consider how you can represent several correct answers in your questions.toml data file. One advantage of the more explicit data structure that you introduced in the previous step is that you can use an array to specify the correct answers as well. Replace each answer key in your TOML file with an answers key that wraps each correct answer within square brackets ([]).

Your questions file will then look something like the following:

```

# questions.toml

[[questions]]
question = "What's the name of the list-like data structure in TOML"
answers = ["Array"]
alternatives = ["List", "Sequence", "Set"]

[[questions]]
question = "How can you run a Python script named quiz.py"
answers = ["python quiz.py", "python -m quiz"]
alternatives = ["python quiz", "python -m quiz.py"]

```

For old questions with only one correct answer, there will be only one answer listed in the answers array. The last question above shows an example of a question with two correct answer alternatives.

Once your data structure is updated, you’ll need to implement the feature in your code as well. You don’t need to make any changes in run_quiz() or prepare_questions(). In ask_question() you need to check that all correct answers are given, while in get_answer(), you need to be able to read multiple answers from the user.

Start with the latter challenge. How can the user enter multiple answers, and how can you validate that each one is valid? One possibility is to enter multiple answers as a comma-separated string. You can then convert the string to a list as follows:

```

>>> answer = "a,b, c"
>>> answer.replace(",", " ").split()
['a', 'b', 'c']

```

You could use .split(",") to split directly on commas. However, first replacing commas with spaces and then splitting on the default whitespace adds some leniency with spaces allowed around the commas. This will be a better experience for your users, as they can write a,b, a, b, or even a b without commas, and your program should interpret it as intended.

The test for valid answers becomes a bit more complicated, though. You therefore replace the tight while loop with a more flexible one. In order to loop until you get a valid answer, you initiate an infinite loop that you return out of once all tests are satisfied. Rename get_answer() to get_answers() and update it as follows:

```
# quiz.py

# ...

def get_answers(question, alternatives, num_choices=1):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

```

Before looking too closely at the details in the code, take the function for a test run:

```

>>> from quiz import get_answers
>>> get_answers(
...     "Pick two numbers", ["one", "two", "three", "four"], num_choices=2
... )
Pick two numbers?
  a) one
  b) two
  c) three
  d) four

Choices (choose 2)? a
Please answer 2 alternatives, separated by comma

Choices (choose 2)? d, e
'e' is not a valid choice. Please use a, b, c, d

Choices (choose 2)? d, b
['four', 'two']

```

Your function first checks that the answer includes the appropriate number of choices. Then each one is checked to make sure it’s a valid choice. If any of these checks fail, then a helpful message is printed to the user.

In the code, you also make some effort to handle the distinction between one and several items when it comes to grammar. You use plural_s to modify text strings to include plural s when needed.

Additionally, you convert the answers to a set to quickly ignore duplicate alternatives. An answer string like "a, b, a" is interpreted as {"a", "b"}.

Finally, note that get_answers() returns a list of strings instead of the plain string returned by get_answer().

Next, you adapt ask_question() to the possibility of multiple correct answers. Since get_answers() already handles most of the complications, what’s left is to check all answers instead of only one. Recall that question is a dictionary with all information about a question, so you don’t need to pass alternatives any longer.

Because the order of the answers is irrelevant, you use set() when comparing the given answers to the correct ones:

You only score a point for the user if they find all the correct answers. Otherwise, you list all correct answers. You can now run your Python quiz application again:

```
$ python quiz.py

Question 1:
How can you run a Python script named quiz.py?
  a) python -m quiz
  b) python quiz
  c) python quiz.py
  d) python -m quiz.py

Choices (choose 2)? a
Please answer 2 alternatives, separated by comma

Choices (choose 2)? a, c
⭐ Correct! ⭐

Question 2:
What's the name of the list-like data structure in TOML?
  a) Array
  b) Set
  c) Sequence
  d) List

Choice? e
'e' is not a valid choice. Please use a, b, c, d

Choice? c
No, the answer is:
- Array

```


Allowing multiple correct answers gives you more flexibility in which kinds of questions you can ask in your quizzes.

> Add Hints to Help the User

Sometimes when you’re asked a question, you need a bit of help to jog your memory. Giving the users the option of seeing a hint can make your quizzes more fun. In this section, you’ll extend your application to include hints.

You can include hints in your questions.toml data file, for example by adding hint as an optional key-value pair:

```
# questions.toml

[[questions]]
question = "How can you run a Python script named quiz.py"
answers = ["python quiz.py", "python -m quiz"]
alternatives = ["python quiz", "python -m quiz.py"]
hint = "One option uses the filename, and the other uses the module name."

[[questions]]
question = "What's a PEP"
answers = ["A Python Enhancement Proposal"]
alternatives = [
    "A Pretty Exciting Policy",
    "A Preciously Evolved Python",
    "A Potentially Epic Prize",
    ]
hint = "PEPs are used to evolve Python."

```
Each question in the TOML file is represented by a dictionary in Python. The new hint fields show up as new keys in those dictionaries. One effect of this is that you don’t need to change how you read the question data, even when you make small changes to your data structure.

Instead, you adapt your code to take advantage of the new optional field. In ask_question() you only need to make one small change:

```
# quiz.py

# ...

def ask_question(question):
    # ...
    answers = get_answers(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    # ...

```

You use question.get("hint") instead of question["hint"] because not all questions come with hints. If one of the question dictionaries doesn’t define "hint" as a key, then question.get("hint") returns None, which is then passed into get_answers().

Again, you’ll make bigger changes to get_answers(). You’ll add the hint as one of the answer alternatives, with a special question mark (?) label:

```

# quiz.py

# ...

def get_answers(question, alternatives, num_choices=1, hint=None):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    if hint:
        labeled_alternatives["?"] = "Hint"

    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle invalid answers
        # ...

        return [labeled_alternatives[answer] for answer in answers]

```

If a hint is provided, then it’s added to the end of labeled_alternatives. The user can then use ? to see the hint printed to the screen. If you test your quiz application, then you’ll now get a bit of friendly help:

```
$ python quiz.py

Question 1:
What's a PEP?
  a) A Potentially Epic Prize
  b) A Preciously Evolved Python
  c) A Python Enhancement Proposal
  d) A Pretty Exciting Policy
  ?) Hint

Choice? ?

HINT: PEPs are used to evolve Python.

Choice? c
⭐ Correct! ⭐

```

In the next section, you’ll add a similar feature. In addition to showing an optional hint before the user answers a question, you’ll show an explanation after they’ve answered it.

> Add Explanations to Reinforce Learning

You can implement explanations similarly to how you implemented hints in the previous section. First, you’ll add an optional explanation field in your data file. Then, in your application, you’ll show the explanation after the user has answered a question.

Start with adding explanation keys in questions.toml:

```
# questions.toml

[[questions]]
question = "What's a PEP"
answers = ["A Python Enhancement Proposal"]
alternatives = [
    "A Pretty Exciting Policy",
    "A Preciously Evolved Python",
    "A Potentially Epic Prize",
    ]
hint = "PEPs are used to evolve Python."
explanation = """
    Python Enhancement Proposals (PEPs) are design documents that provide
    information to the Python community. PEPs are used to propose new features
    for the Python language, to collect community input on an issue, and to
    document design decisions made about the language.
"""

[[questions]]
question = "How can you add a docstring to a function"
answers = [
    "By writing a string literal as the first statement in the function",
    "By assigning a string to the function's .__doc__ attribute",
]
alternatives = [
    "By using the built-in @docstring decorator",
    "By returning a string from the function",
]
hint = "They're parsed from your code and stored on the function object."
explanation = """
    Docstrings document functions and other Python objects. A docstring is a
    string literal that occurs as the first statement in a module, function,
    class, or method definition. Such a docstring becomes the .__doc__ special
    attribute of that object. See PEP 257 for more information.

    There is no built-in @docstring decorator. Many functions naturally return
    strings. Such a feature can therefore not be used for docstrings.
"""

```


TOML supports multiline strings by using triple quotes (""") in the same way as Python. These are great for explanations that may span a few sentences.

The explanations will be printed to the screen after the user has answered a question. In other words, the explanations aren’t part of the user interaction done in get_answers(). Instead, you’ll print them inside ask_question():

Because you print the explanation after giving the user feedback on whether their answer was correct or not, you can’t return inside the if … else block any longer. You therefore move the return statement to the end of the function.

Your explanations look something like the following when you run your quiz application:

```
$ python quiz.py

Question 1:
How can you add a docstring to a function?
  a) By returning a string from the function
  b) By assigning a string to the function's .__doc__ attribute
  c) By writing a string literal as the first statement in the function
  d) By using the built-in @docstring decorator
  ?) Hint

Choices (choose 2)? a, b
No, the answers are:
- By writing a string literal as the first statement in the function
- By assigning a string to the function's .__doc__ attribute

EXPLANATION:
    Docstrings document functions and other Python objects. A docstring is a
    string literal that occurs as the first statement in a module, function,
    class, or method definition. Such a docstring becomes the .__doc__ special
    attribute of that object. See PEP 257 for more information.

    There is no built-in @docstring decorator. Many functions naturally return
    strings. Such a feature can therefore not be used for docstrings.
```

find the complete codes below:

```
# questions.toml

[[questions]]
question = "When was the first known use of the word 'quiz'"
answers = ["1781"]
alternatives = ["1771", "1871", "1881"]

[[questions]]
question = "Which built-in function can get information from the user"
answers = ["input"]
alternatives = ["get", "print", "write"]

[[questions]]
question = "What's the purpose of the built-in zip() function"
answers = ["To iterate over two or more sequences at the same time"]
alternatives = [
    "To combine several strings into one",
    "To compress several files into one archive",
    "To get information from the user",
]

[[questions]]
question = "What does dict.get(key) return if key isn't found in dict"
answers = ["None"]
alternatives = ["key", "True", "False"]

[[questions]]
question = "How do you iterate over both indices and elements in an iterable"
answers = ["enumerate(iterable)"]
alternatives = [
    "enumerate(iterable, start=1)",
    "range(iterable)",
    "range(iterable, start=1)",
]

[[questions]]
question = "What's the official name of the := operator"
answers = ["Assignment expression"]
alternatives = ["Named expression", "Walrus operator", "Colon equals operator"]

[[questions]]
question = "What's one effect of calling random.seed(42)"
answers = ["The random numbers are reproducible."]
alternatives = [
    "The random numbers are more random.",
    "The computer clock is reset.",
    "The first random number is always 42.",
]

[[questions]]
question = "When does __name__ == '__main__' equal True in a Python file"
answers = ["When the file is run as a script"]
alternatives = [
    "When the file is imported as a module",
    "When the file has a valid name",
    "When the file only has one function",
]

[[questions]]
question = "Which version of Python is the first with TOML support built in"
answers = ["3.11"]
alternatives = ["3.9", "3.10", "3.12"]

[[questions]]
question = "What's the name of the list-like data structure in TOML"
answers = ["Array"]
alternatives = ["List", "Sequence", "Set"]

[[questions]]
question = "How can you run a Python script named quiz.py"
answers = ["python quiz.py", "python -m quiz"]
alternatives = ["python quiz", "python -m quiz.py"]
hint = "One option uses the filename, and the other uses the module name."

[[questions]]
question = "What's a PEP"
answers = ["A Python Enhancement Proposal"]
alternatives = [
    "A Pretty Exciting Policy",
    "A Preciously Evolved Python",
    "A Potentially Epic Prize",
]
hint = "PEPs are used to evolve Python."
explanation = """
    Python Enhancement Proposals (PEPs) are design documents that provide
    information to the Python community. PEPs are used to propose new features
    for the Python language, to collect community input on an issue, and to
    document design decisions made about the language.
"""

[[questions]]
question = "How can you add a docstring to a function"
answers = [
    "By writing a string literal as the first statement in the function",
    "By assigning a string to the function's .__doc__ attribute",
]
alternatives = [
    "By using the built-in @docstring decorator",
    "By returning a string from the function",
]
hint = "They are parsed from your code and stored on the function object."
explanation = """
    Docstrings document functions and other Python objects. A docstring is a
    string literal that occurs as the first statement in a module, function,
    class, or method definition. Such a docstring becomes the .__doc__ special
    attribute of that object. See PEP 257 for more information.

    There is no built-in @docstring decorator. Many functions naturally return
    strings. Such a feature can therefore not be used for docstrings.
"""

```

for quiz.py:

```

# quiz.py

import pathlib
import random
from string import ascii_lowercase
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))

    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    return 1 if correct else 0

def get_answers(question, alternatives, num_choices=1, hint=None):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    if hint:
        labeled_alternatives["?"] = "Hint"

    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

if __name__ == "__main__":
    run_quiz()

```

In the final step, you’ll add one more feature: support for several quiz topics within your application.

### Step 6: Support Several Quiz Topics

In this section, you’ll make one final improvement that will make your Python quiz application more fun, varied, and interesting. You’ll add the option of grouping questions into different topics and letting your users pick which topic they’ll be quizzed about.

More topics and new questions will keep your quiz application fresh. 

Sections in TOML files can be nested. You create nested tables by adding periods (.) in the section headers. As an illustrative example, consider the following TOML document:

```
>>> toml = """
... [python]
... label = "Python"
...
... [python.version]
... number = "3.10"
... release.date = 2021-10-04
... release.manager = "@pyblogsal"
... """

>>> import tomli
>>> tomli.loads(toml)
{'python': {'label': 'Python', 'version': {
    'release': {'date': datetime.date(2021, 10, 4), 'manager': '@pyblogsal'},
    'number': '3.10'}}}
```

Here, the section header [python.version] is represented as version nested within python. Similarly, keys with periods are also interpreted as nested dictionaries, as evidenced by release in this example.

You can reorganize questions.toml to include a section for each topic. In addition to the nested questions arrays, you’ll add a label key that provides a name for each topic. Update your data file to use the following format:

```
# questions.toml

[python]
label = "Python"

[[python.questions]]
question = "How can you add a docstring to a function"
answers = [
    "By writing a string literal as the first statement in the function",
    "By assigning a string to the function's .__doc__ attribute",
]
alternatives = [
    "By using the built-in @docstring decorator",
    "By returning a string from the function",
]
hint = "They're parsed from your code and stored on the function object."
explanation = """
    Docstrings document functions and other Python objects. A docstring is a
    string literal that occurs as the first statement in a module, function,
    class, or method definition. Such a docstring becomes the .__doc__ special
    attribute of that object. See PEP 257 for more information.

    There's no built-in @docstring decorator. Many functions naturally return
    strings. Such a feature can therefore not be used for docstrings.
"""

[[python.questions]]
question = "When was the first public version of Python released?"
answers = ["February 1991"]
alternatives = ["January 1994", "October 2000", "December 2008"]
hint = "The first public version was labeled version 0.9.0."
explanation = """
    Guido van Rossum started work on Python in December 1989. He posted
    Python v0.9.0 to the alt.sources newsgroup in February 1991. Python
    reached version 1.0.0 in January 1994. The next major versions,
    Python 2.0 and Python 3.0, were released in October 2000 and December
    2008, respectively.
"""

[capitals]
label = "Capitals"

[[capitals.questions]]
question = "What's the capital of Norway"
answers = ["Oslo"]
hint = "Lars Onsager, Jens Stoltenberg, Trygve Lie, and Børge Ousland."
alternatives = ["Stockholm", "Copenhagen", "Helsinki", "Reykjavik"]
explanation = """
    Oslo was founded as a city in the 11th century and established as a
    trading place. It became the capital of Norway in 1299. The city was
    destroyed by a fire in 1624 and rebuilt as Christiania, named in honor
    of the reigning king. The city was renamed back to Oslo in 1925.
"""

[[capitals.questions]]
question = "What's the state capital of Texas, USA"
answers = ["Austin"]
alternatives = ["Harrisburg", "Houston", "Galveston", "Columbia"]
hint = "SciPy is held there each year."
explanation = """
    Austin is named in honor of Stephen F. Austin. It was purpose-built to
    be the capital of Texas and was incorporated in December 1839. Houston,
    Harrisburg, Columbia, and Galveston are all earlier capitals of Texas.
"""

```

Now, there are two topics included in the data file: Python and Capitals. Within each topic section, the question tables are still structured the same as before. This means that the only change you need to make is how you prepare the questions.

You start by reading and parsing questions.toml. Next, you pick out each topic and store it in a new, temporary dictionary. You need to ask the user about which topic they’d like to try. Luckily, you can reuse get_answers() to get input about this. Finally, you pick out the questions belonging to the chosen topic and shuffle them up:


```

# quiz.py

# ...

def prepare_questions(path, num_questions):
    topic_info = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in topic_info.values()
    }
    topic_label = get_answers(
        question="Which topic do you want to be quizzed about",
        alternatives=sorted(topics),
    )[0]

    questions = topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

```

The data structure returned by prepare_questions() is still the same as before, so you don’t need to make any changes to run_quiz(), ask_question(), or get_answers(). When these kinds of updates only require you to edit one or a few functions, that’s a good sign indicating that your code is well-structured, with good abstractions.

Run your Python quiz application. You’ll be greeted by the new topic prompt:

```

$ python quiz.py
Which topic do you want to be quizzed about?
  a) Capitals
  b) Python

Choice? a

Question 1:
What's the capital of Norway?
  a) Reykjavik
  b) Helsinki
  c) Stockholm
  d) Copenhagen
  e) Oslo
  ?) Hint

Choice? ?

HINT: Lars Onsager, Jens Stoltenberg, Trygve Lie, and Børge Ousland.

Choice? e
⭐ Correct! ⭐

EXPLANATION:
    Oslo was founded as a city in the 11th century and established as a
    trading place. It became the capital of Norway in 1299. The city was
    destroyed by a fire in 1624 and rebuilt as Christiania, named in honor
    of the reigning king. The city was renamed back to Oslo in 1925.

```

This ends the guided part of this journey. You’ve created a powerful Python quiz application in the terminal. You can see the complete source code as well as a list of questions below:

```
[python]
label = "Python"

[[python.questions]]
question = "When was the first known use of the word 'quiz'"
answers = ["1781"]
alternatives = ["1771", "1871", "1881"]

[[python.questions]]
question = "Which built-in function can get information from the user"
answers = ["input"]
alternatives = ["get", "print", "write"]

[[python.questions]]
question = "What's the purpose of the built-in zip() function"
answers = ["To iterate over two or more sequences at the same time"]
alternatives = [
    "To combine several strings into one",
    "To compress several files into one archive",
    "To get information from the user",
]

[[python.questions]]
question = "What does dict.get(key) return if key isn't found in dict"
answers = ["None"]
alternatives = ["key", "True", "False"]

[[python.questions]]
question = "How do you iterate over both indices and elements in an iterable"
answers = ["enumerate(iterable)"]
alternatives = [
    "enumerate(iterable, start=1)",
    "range(iterable)",
    "range(iterable, start=1)",
]

[[python.questions]]
question = "What's the official name of the := operator"
answers = ["Assignment expression"]
alternatives = [
    "Named expression",
    "Walrus operator",
    "Colon equals operator",
]

[[python.questions]]
question = "What's one effect of calling random.seed(42)"
answers = ["The random numbers are reproducible."]
alternatives = [
    "The random numbers are more random.",
    "The computer clock is reset.",
    "The first random number is always 42.",
]

[[python.questions]]
question = "Which version of Python is the first with TOML support built in"
answers = ["3.11"]
alternatives = ["3.9", "3.10", "3.12"]

[[python.questions]]
question = "How can you run a Python script named quiz.py"
answers = ["python quiz.py", "python -m quiz"]
alternatives = ["python quiz", "python -m quiz.py"]
hint = "One option uses the filename, and the other uses the module name."

[[python.questions]]
question = "What's the name of the list-like data structure in TOML"
answers = ["Array"]
alternatives = ["List", "Sequence", "Set"]

[[python.questions]]
question = "What's a PEP"
answers = ["A Python Enhancement Proposal"]
alternatives = [
    "A Pretty Exciting Policy",
    "A Preciously Evolved Python",
    "A Potentially Epic Prize",
]
hint = "PEPs are used to evolve Python."
explanation = """
Python Enhancement Proposals (PEPs) are design documents that provide
information to the Python community. PEPs are used to propose new features
for the Python language, to collect community input on an issue, and to
document design decisions made about the language.
"""

[[python.questions]]
question = "How can you add a docstring to a function"
answers = [
    "By writing a string literal as the first statement in the function",
    "By assigning a string to the function's .__doc__ attribute",
]
alternatives = [
    "By using the built-in @docstring decorator",
    "By returning a string from the function",
]
hint = "They are parsed from your code and stored on the function object."
explanation = """
Docstrings document functions and other Python objects. A docstring is a
string literal that occurs as the first statement in a module, function,
class, or method definition. Such a docstring becomes the .__doc__ special
attribute of that object. See PEP 257 for more information.

There's no built-in @docstring decorator. Many functions naturally return
strings. Such a feature can therefore not be used for docstrings.
"""

[[python.questions]]
question = "When was the first public version of Python released"
answers = ["February 1991"]
alternatives = ["January 1994", "October 2000", "December 2008"]
hint = "The first public version was labeled version 0.9.0."
explanation = """
Guido van Rossum started work on Python in December 1989. He posted
Python v0.9.0 to the alt.sources newsgroup in February 1991. Python
reached version 1.0.0 in January 1994. The next major versions,
Python 2.0 and Python 3.0, were released in October 2000 and December
2008, respectively.
"""

[capitals]
label = "Capitals"

[[capitals.questions]]
question = "What's the capital of Norway"
answers = ["Oslo"]
hint = "Lars Onsager, Jens Stoltenberg, Trygve Lie, and Børge Ousland."
alternatives = ["Stockholm", "Copenhagen", "Helsinki", "Reykjavik"]
explanation = """
Oslo was founded as a city in the 11th century and established as a
trading place. It became the capital of Norway in 1299. The city was
destroyed by a fire in 1624 and rebuilt as Christiania, named in honor
of the reigning king. The city was renamed back to Oslo in 1925.
"""

[[capitals.questions]]
question = "What's the state capital of Texas, USA"
answers = ["Austin"]
alternatives = ["Harrisburg", "Houston", "Galveston", "Columbia"]
hint = "SciPy is held there each year."
explanation = """
Austin is named in honor of Stephen F. Austin. It was purpose-built to
be the capital of Texas and was incorporated in December 1839. Houston,
Harrisburg, Columbia, and Galveston are all earlier capitals of Texas.
"""

```

```

# quiz.py

import pathlib
import random
from string import ascii_lowercase
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(path, num_questions):
    topic_info = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in topic_info.values()
    }
    topic_label = get_answers(
        question="Which topic do you want to be quizzed about",
        alternatives=sorted(topics),
    )[0]

    questions = topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))

    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    return 1 if correct else 0

def get_answers(question, alternatives, num_choices=1, hint=None):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    if hint:
        labeled_alternatives["?"] = "Hint"

    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

if __name__ == "__main__":
    run_quiz()

```

### Conclusion

Good job! You’ve created a flexible and useful quiz application with Python. Along the way, you’ve learned how you can start with a basic script and build it out to a more complex program.

In this tutorial, you’ve learned how to:

* Interact with the user in the terminal
* Improve the usability of your application
* Refactor your application to continuously improve it
* Store data in dedicated data files

Now, go have some fun with your quiz application. Add some questions on your own, and challenge your friends. Share your best questions and quiz topics in the comments below!

### Next Steps

As you’ve followed along in this tutorial, you’ve created a well-featured quiz application. However, there’s still ample opportunity to improve on the project.

Here are some ideas for additional features:

- Quiz creator: Add a separate application that interactively asks for questions and answers and stores them in the proper TOML format.
- Store data in a database: Replace the TOML data file with a proper database.
- Question Hub: Create a central questions database online that your application can connect to.
- Multiuser challenges: Allow different users to challenge each other in a trivia competition.

You can also reuse the logic in this quiz application but change the front-end presentation layer. Maybe you can convert the project to a web application. Feel free to share your improvements with me!.