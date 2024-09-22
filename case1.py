import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 10  # Максимальное количество попыток

    print("Я загадал число от 1 до 100. Угадайте его!")

    while attempts > 0:
        try:
            guess = int(input("Введите ваше предположение: "))
            
            if guess < 1 or guess > 100:
                print("Число должно быть в диапазоне от 1 до 100.")
                continue
            
            if guess < number_to_guess:
                print("Слишком маленькое число.")
            elif guess > number_to_guess:
                print("Слишком большое число.")
            else:
                print("Поздравляю! Вы угадали число!")
                break

            attempts -= 1
            print(f"Осталось попыток: {attempts}")

        except ValueError:
            print("Ошибка: введите корректное целое число.")

    if attempts == 0:
        print(f"Вы исчерпали все попытки. Загаданное число было: {number_to_guess}")

if __name__ == "__main__":
    guess_number()