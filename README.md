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
$ python quiz.py
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
$ python quiz.py

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
