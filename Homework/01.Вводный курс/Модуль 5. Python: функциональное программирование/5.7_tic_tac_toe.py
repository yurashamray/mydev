"""
Курс: MIFIIB
Модуль.5.Python
Игровое практическое задание - «Крестики-нолики»
Выполнил: Yuriy Shamray

"""
from colorama import Fore, Style # Импортируем модуль colorama для цветного вывода

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

# Создаем словарь для игрового поля
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


board_keys = [] # Создаем пустой список для ключей игрового поля

for i in theBoard: # Перебираем ключи словаря и добавляем их в список
    board_keys.append(i)


# Функция для отображения игрового поля
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X' # Инициализируем текущего игрока
    count = 0 # Инициализируем счетчик ходов

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
            print(Fore.YELLOW + "Место уже занято! Выберите другую клетку!", Style.RESET_ALL)
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

                
        if count == 9: # Если доска заполнена, то объявляем ничью
            print("\nИгра Окончена!")
            print(Fore.YELLOW + "Ничья!", Style.RESET_ALL)
            break

        
        if turn == 'X': # Смена игрока после каждого хода
            turn = 'O'
        else:
            turn = 'X'

           
    restart = input("\nНовая Игра?(y/n)") # Запрашиваем у пользователя, хочет ли он сыграть еще раз
    if restart == 'y' or restart == 'Y': # Если пользователь соглашается, то очищаем поле и начинаем новую игру
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == '__main__':
    game()
