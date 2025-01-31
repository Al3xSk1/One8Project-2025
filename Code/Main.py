# Programmers: Alexander P. Kovalski, Elijah A. F. Turcotte, Jordan E. Real
# Date Last Modified: 30JAN2025
# Purpose: Make winning educational project by teaching students Sigma Notation
# Function: Using globals, functions, input, and iteration to create a game that teaches students how to do sigma notation.


# Imports
import turtle as trtl
import random as rand
import time


# Define Global Vars
debugMode = False
score = 0
gameOver = False
listOfQuestionNum = []
participant = trtl.Turtle()
participant.fillcolor("red")
participant.begin_fill()
participant.penup()
participant.goto(-100, 0)
participant.pendown()
wn = trtl.Screen()


# Instructions
def instructions():
  print("Welcome to Sigma Games!")
  print("In this game, you will be given a random equation.")
  print("You will have to solve the equation by using Sigma Notation.")
  print("You will have to answer the questions with the correct answer.")
  print("If you do you will connect another dot!")
  print("If you get the question right, you will be given a new equation.")
  print("If you get the question wrong, you will be given a explanation if you would like and be given a new question.")
  


#  Display the connect the dots on the screen
def display():
  global gameOver
  global score
  if (score == 1):
    participant.goto(-90, 20)
  elif (score == 2):
    participant.goto(-60, 40)
  elif (score == 3):
    participant.goto(-30, 45)
  elif (score == 4):
    participant.goto(10, 100)
  elif (score == 5):
    participant.goto(0, 50)
  elif (score == 6):
    participant.goto(40, 45)
  elif (score == 7):
    participant.goto(60, 30)
  elif (score == 8):
    participant.goto(90, 10)
  elif (score == 9):
    participant.goto(120, 30)
  elif (score == 10):
    participant.goto(120, -30)
  elif (score == 11):
    participant.goto(90, -10)
  elif (score == 12):
    participant.goto(60, -30)
  elif (score == 13):
    participant.goto(-30, -35)
  elif (score == 14):
    participant.goto(0, -60)
  elif (score == 15):
    participant.goto(-45, -35)
  elif (score == 16):
    participant.goto(-60, -30)
  elif (score == 17):
    participant.goto(-80, -20)
  elif (score == 18):
    participant.goto(-100, 0)
    participant.end_fill()
  elif (score == 19):
    participant.penup()
    participant.goto(-80, 20)
    participant.pensize(3)
    participant.dot()
    participant.hideturtle()
    gameOver = True




# Calculate Answer Formula
def sigma_formula(n):
  sum = n * (n + 1) / 2
  return sum




# Explaining the why you got the answer wrong
def explain(n):
  print(f"--- Sigma of {n} ---")
  print(
      "The Sigma Notation is a way of writing down the sum of a sequence of numbers."
  )
  sum = int(sigma_formula(n))
  time.sleep(1)
  print("The Sigma Notation is written as follows: ")
  time.sleep(1)
  print("Sigma(n) = n * (n + 1) / 2")
  time.sleep(1)
  print(
      f"Therefore the , the Sigma Notation of {n} is {n} * ({n} + 1) / 2 = {sum}"
  )




# A Single execution of a question
def game(answer, n):
  global gameover
  global score
  global listOfQuestionNum
  answer = int(answer)
  if answer == sigma_formula(n):
    print("Correct")
    score = score + 1
    listOfQuestionNum.append(n)
    display()
  else:
    print("Incorrect")
    explanation = input("Would you like an explanation? (y/n) ")
    if (explanation == "y"):
      explain(n)
  print()




# Main Loop for executing a game instance
def main():
  global score
  global gameOver
  global listOfQuestionNum
  global debugMode
  instructions()
  if (not debugMode):
    while (not gameOver):
      n = 0
      if (score > 16):
        n = rand.randint(11, 16)
      elif (score > 8):
        n = rand.randint(6, 11)
      else:
        n = rand.randint(2, 6)
      print("What is the sum of all the numbers from 1 to", n)
      answer = input()
      game(answer, n)
  else:
    while (not gameOver):
      score = score + 1
      display()
  if (gameOver):
    print("Game Over")
    print("You got", score, "correct")
    sum = 0
    for i in listOfQuestionNum:
      sum = sum + i
    print(f"You summed up this total {sum}")




# Calling the Main (Loop) Function
main()


wn.mainloop()


