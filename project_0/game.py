"""Guess the number"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Guess the number
    Args:
        number (int, optional): Generated number. Defaults to 1.
    Returns:
        int: Number of attempts
    """
    count = 0 # Attempt counter
    predict_number_min = 1 # lower limit of number search
    predict_number_max = 101 # upper limit of number search
    
    while True:
        count += 1
        
        predict_number = (predict_number_max + predict_number_min) // 2
        
        if number > predict_number:
            predict_number_min = predict_number # carrying the lower limit of the search for a number
            
        elif number < predict_number:
            predict_number_max = predict_number # carrying the upper limit of the search for a number
            
        else:
            break  # exit from the loop
    return count


def score_game(random_predict) -> int:
    """Calculation of the average number of attempts for which the search algorithm works.
       Based on 1000 passes.
    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # fix seed
    random_array = np.random.randint(1, 101, size=(10000))  # given a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in {score} attempts on average")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)