"""
Курс: MIFIIB
Модуль.5.Python
Игровое практическое задание - «Крестики-нолики»
Выполнил: Юрий Шамрай (yura.shamray@gmail.com)

"""
from colorama import Fore, Style

# Правила игры
print(Fore.GREEN + '*********************************************', Style.RESET_ALL)
print(Fore.GREEN + '*************' + Style.RESET_ALL + '| КРЕСТИКИ-НОЛИКИ |' + Fore.GREEN + '*************\n'
      '            Карта игровых клеток:\n' 
      '                   7|8|9\n' 
      '                   -+-+-\n' 
      '                   4|5|6\n' 
      '                   -+-+-\n' 
      '                   1|2|3\n' + Style.RESET_ALL +
      'Введите номер клетки, куда поставить X или 0\n' +
      Fore.GREEN + '*********************************************', Style.RESET_ALL)

# Словарь для игрового поля
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


board_keys = []

for i in theBoard:
    board_keys.append(i)


# Игровое поле
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(theBoard)
        print("Ход игрока - " + turn + ". Введите номер клетки от 1 до 9:")

        move = input()

        assert move in ['1', '2', '3', '4', '5', '6', '7', '8',
                        '9'], 'ОШИБКА! ' + move + ' не в интервале от 1 до 9)'

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print(Fore.YELLOW + "Место уже занято! Выберите другую позицию!", Style.RESET_ALL)
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # верхние позиции
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # средние позиции
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # нижнии позиции
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # по левой стороне
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # по центру
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # по правой стороне
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # по диагонали
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # по диагонали
                printboard(theBoard)
                print("\nИгра Окончена!")
                print(Fore.GREEN + "**** Игрок " + turn + " выиграл! ****", Style.RESET_ALL)
                break

                # Если ни X, ни O не выиграют и доска будет заполнена, тогда результат «Ничья».
        if count == 9:
            print("\nИгра Окончена!")
            print(Fore.YELLOW + "Ничья!", Style.RESET_ALL)
            break

        # Смена игрока после каждого хода.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Запрашиваем, хочет ли игрок перезапустить игру или нет.
    restart = input("\nНовая Игра?(y/n)")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == '__main__':
    game()
