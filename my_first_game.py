import random
import sys
import time

def print_typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def play_game():
    print_typewriter("Добро пожаловать в игру Угадай число")
    
    # Запускаем бесконечный цикл для перезапуска всей игры
    while True:
        print_typewriter("\nЯ загадал число от 1 до 10. Попробуй угадать")
        secret_number = random.randint(1, 10)
        
        attempts = 0
        lives = 3  # переменая (жизни

        # Этот цикл крутится, пока у игрока есть жизни
        while lives > 0:
            print_typewriter(f"\nВведите ваше предположение (Осталось жизней: {lives}): ", delay=0.01
            try:
                guess = int(input())
            except ValueError:
                print_typewriter("Пожалуйста, введите целое число.")
                continue

            attempts += 1

            if guess < secret_number:
                print_typewriter("Слишком мало")
                lives = lives - 1  #-1 попытка
            elif guess > secret_number:
                print_typewriter("Слишком много")
                lives = lives - 1  #-1 попытка
            else:
                print_typewriter(f"Поздравляю, вы угадали число {secret_number}")
                print_typewriter(f"Количество попыток: {attempts}")
                break 

        # Если цикл угадывания закончился, а число так и не угадали — значит, жизни кончились
        if lives == 0:
            print_typewriter(f"Вы проиграли! Жизни закончились. Было загадано число {secret_number}")

        # Спрашиваем про рестрарт всей игры
        print_typewriter("\nRestart (да/нет)?", delay=0.01)
        answer = input().lower()
        
        if answer != "да":
            print_typewriter("Спасибо за игру! До встречи!")
            break  # Выходим из самого главного цикла и закрываем программу

if __name__ == "__main__":
    play_game()