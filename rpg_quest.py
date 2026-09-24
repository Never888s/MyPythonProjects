import sys
import time
import random


def print_typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_game():
    print_typewriter("⚔️ ДОБРО ПОЖАЛОВАТЬ В ТЕКСТОВОЕ ПРИКЛЮЧЕНИЕ ⚔️")
    print_typewriter("--------------------------------------------")

    #характреристики персонажа
    hp = 100
    gold = 10

    print_typewriter(f"вы проснулись посреди леса, у вас {hp} здоровья и {gold} золота.")
    print_typewriter("Вы встаете и видите перед собой два пути")
    print_typewriter("1. узкая тропа которая ведет вас в пещеру")
    print_typewriter("2. широкая дорого, ведущая к старому замку")

    while True:
        print_typewriter("выберите путь (1 или 2):", delay = 0.03)
        choice = input().strip()

        if choice == "1":
            cave_location(hp, gold)
            break
        elif choice == "2":
            castle_location(hp, gold)
            break
        else:
            print_typewriter("Неизвестная тропа. Пожалуйста, выберите 1 или 2.", delay = 0.03)

def cave_location(hp, gold):
    print_typewriter("\n🦇 ПЕЩЕРА 🦇")
    print_typewriter("Вы аккуратно заходите в пещеру. Под вашими ногами хрустят кости.")
    print_typewriter("Вдруг из темноты появляеться летучвая мышь и нападает на вас!")

    hp = hp - 20
    print_typewriter(f"💥 Бам! Вы потеряли 20 ХП. Теперь у вас {hp} ХП.")
    print_typewriter("Зато на полу вы заметили блестящий мешочек с золотом.")

    gold = gold + 15
    print_typewriter(f"💰 Вы подобрали мешочек! Теперь у вас {gold} монет.")

    #тут конец игры, можно добавить продолжение или возвращение в начало

def castle_location(hp, gold):
    print_typewriter("\n 🏰 ЗАМОК 🏰")
    print_typewriter("Вы подходите к тяжелым воротам замка. Вас встречает стражник.")
    print_typewriter("Стражник говорит вам: 'У вас есть золото для входа?'")

    if gold >= 5:
        gold = gold - 5
        print_typewriter(f"Вы платите 5 монет. У вас осталось {gold} монет.")
        print_typewriter("Стражник пропускает вас внутрь замка. Вы видите роскошные залы и драгоценности.")
        print_typewriter("Внутри замка тепло и горит костер. Вы восстановили 10 ХП!")
        print_typewriter("вы видете не известную комнату.")
        print_typewriter("хотите войти в нее? (да/нет)", delay=0.03)
        choice = input().strip().lower()

        if choice == "да":
            hp = hp + 10
            print_typewriter(f"Теперь у вас {hp} ХП.")
    else:
        print_typewriter("😡 У вас нет денег! Стражник бьет вас щитом и прогоняет.")
        hp = hp - 30
        print_typewriter(f"💥 У вас осталось всего {hp} ХП.")

    boss_battle(hp, gold)


def boss_battle(hp, gold):
    print_typewriter("\n👹ЛОГОВО БОССА👹")
    print_typewriter("перед вами садиться дракон!")
    print_typewriter("Он преграждает вам путь, но вместо драки ухмыляется и говорит:")
    print_typewriter("Я не буду сжигать тебя просто так. Сыграем в игру!")
    print_typewriter("Я загадал тайное число от 1 до 10. У тебя есть ровно 3 жизни.")
    print_typewriter("Угадаешь — заберешь всё мое золото. Проиграешь — станешь моим обедом!")

    while True:
        print_typewriter("\nТы принимаешь вызов дракона? (да/нет)", delay=0.03)
        accept = input().strip().lower()

        if accept == "да":
            print_typewriter("\n🔥 Дракон сужает глаза: 'Отлично! Твоя первая попытка...'")
            break
        elif accept == "нет":
            print_typewriter("\nДракон удивленно приподнимает бровь: 'Оу, какая жалость...'")
            print_typewriter("💀 Игра окончена! Никогда не отказывайтесь от игры с драконами.")
            return ## Мгновенно прерываем всю функцию boss_battle, и возвращаемся в start_game
        else:
            print_typewriter("Дракон не понимает твоего языка, ответьте 'да' или 'нет'.", delay=0.01)

    #если игрок ответил да его перебросит сюда
    boss_secret_number = random.randint(1, 10)
    boss_lives = 3
    boss_attempt = 0

    while boss_lives > 0:
        print_typewriter(f"\nУ тебя осталовось {boss_lives} жизни. введи число от 1 до 10:", delay=0.01)
        try:
            player_guess = int(input().strip())
        except ValueError:
            print_typewriter("Пожалуйста, введи число от 1 до 10")
            continue

        boss_attempt += 1

        if player_guess < boss_secret_number:
            print_typewriter("Дракон ухмыляется: 'Мое число больше!'")
            boss_lives -= 1
            print_typewriter(f"У тебя осталось {boss_lives} жизни.")
        elif player_guess > boss_secret_number:
            print_typewriter("Дракон ухмыляется: 'Мое число меньше!'")
            boss_lives -= 1
            print_typewriter(f"У тебя осталось {boss_lives} жизни.")
        else:
            print_typewriter("🎉 Поздравляю! Ты угадал число дракона!")
            print_typewriter(f"Ты выиграл {gold} монет дракона!")
            print_typewriter(f"🏆 Дракон в шоке падает на колени! Вы затратили попыток: {boss_attempt}")
            break

        if boss_lives > 0:
            print_typewriter("🏆 ВЫ УСПЕШНО ПРОШЛИ ИГРУ И СТАЛИ БОГАТЫМ ГЕРОЕМ!")
        else:
            print_typewriter(f"\n💀 Дракон широко открывает пасть: 'Жизни закончились! Я загадал число {boss_secret_number}!'")
            print_typewriter("🔥 БУУУУМ! Вас поглотило пламя... Игра окончена.")

if __name__ == "__main__":
    start_game()
