# Project 0. Guess the number / Угадай число

## Contents
[1. Description of the projects]()

[2. What problem are we solving?]()

[3. Information about the input and output information]()

[4. Stages of work on the project]()

[5. Result]()

[6. Conclusion]()


### 1. Description of the projects
The program guesses a random number after a certain number of attempts

:arrow_up: [Go to contents](https://github.com/lukashinin/learning_projects/blob/main/project_0/README.md#Contents)

### 2. What problem are we solving?
You need to write a program that finds a randomly generated number in an array of numbers in the minimum number of attempts. The search algorithm should find a number in less than 20 attempts.

#### Working conditions:
- The computer generates a random number, a number from 0 to 100. You need to write a function that will look for the desired number in the array.
- The search algorithm is "Binary Search"
- It is necessary that the program guesses the number in less than 20 attempts.

#### Quality metric
Results are measured by the average number of attempts at 1000 repetitions. The minimum number of attempts must be achieved.

### 3. Information about the input and output information
There is no input as the program generates a random number from numpy in the body of the program.
The output is the average number of attempts for which the written algorithm finds a number.

### 4. Stages of work on the project

### 5. Result
Correctly working program

### 6. Conclusion
The "Binary Search" algorithm finds on average a number in a sorted array in 5 attempts