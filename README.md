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

next, the python REPL will come up in the terminal.

run the below code

```
>>> name = input("What's your name? ")
What's your name? John Deo

>>> name
'John Deo'

```

