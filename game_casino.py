from random import randint, choice

def casino():
    my_money = 1000
    digit_win = randint(1, 30)

    while True:
        if my_money <= 0:
            print("Вы проиграли!")
            break
        stavka = int(input("Сколько сомов поставите? -"))
        if my_money >= stavka:
            change_digit = int(input("Выберите слот от 1 до 30 включительно: "))
            if 0 < change_digit <= 30:
                if digit_win == change_digit:
                    my_money = (stavka * 2)
                    print(f'Вы угадали! Ваши капитал на данное время:  {my_money}')
                else:
                    my_money -= stavka
                    print("Вы не угадали, ваш капитал: ", my_money)

                user_input = input(f"Желаете еще сыграть? Да или Нет: ").lower()
                if user_input == "нет":
                    if my_money > 1000:
                        print(f"Вы выиграли, ваш капитал {my_money}")
                    else:
                        print(f"Вы проиграли {1000 - my_money}\n"
                              f"У вас осталось: {my_money}")
                    break
            else:
                print('Введите число только от 1 до 30 включительно')
        else:
            print('Поставьте сумму денег не превышающий ваш капитал')
