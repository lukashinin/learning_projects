"""Guess the number ver. 2.

"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0 # Счетчик попыток
    predict_number_min = 1 # нижняя граница поиска числа
    predict_number_max = 101 # верхняя граница поиска числа
    
    while True:
        count += 1
        
        predict_number = (predict_number_max + predict_number_min) // 2
        
        if number > predict_number:
            predict_number_min = predict_number # смещение нижней границы поиска числа
            
        elif number < predict_number:
            predict_number_max = predict_number # смещение верхней границы поиска числа
            
        else:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)