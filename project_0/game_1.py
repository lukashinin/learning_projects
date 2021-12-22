"""Guess the number"""
import numpy as np

number = np.random.randint(1,101) #generate the number

count = 0 #number of attemps

while True:
    count+=1
    predict_number = int(input('Guess a number from 1 to 100 '))
    
    if predict_number < number:
        print('The guessed number is greater than the entered number')    
        
    elif predict_number > number:
        print('The guessed number is less than the entered number')
    
    else: 
        print(f'You guessed the number! This number is {number}, you used {count} attempts. See you!')
        break #End of the game. Exiting the loop
print('saffafa') 