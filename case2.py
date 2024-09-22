import math

def calculate_factorial(n):
    return math.factorial(n)

#  своя реализация
#  def calculate_factorial(n):
#     if n < 0:
#         return "Ошибка: факториал для отрицательных чисел не определен."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result


def main():
    while True:
        user_input = input("Введите положительное целое число: ")
        
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: число должно быть положительным.")
                continue
            
            result = calculate_factorial(number)
            print(f"Факториал числа {number} равен {result}.")
            break
        
        except ValueError:
            print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()