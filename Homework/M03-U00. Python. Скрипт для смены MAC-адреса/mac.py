#!/usr/bin/env python
#
# Скрипт для смены MAC-адреса в Linux
# Yuriy Shamray - MIFIIB
#
# Подключаем модули
import subprocess
import argparse
import random
import string
import re
import os
from tqdm import tqdm, trange
import colorama
from time import sleep
from colorama import Fore, Style

# Шаблон для проверки MAC-адреса
valid_mac_pattern = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"

# Функция для проверки запущен ли скрипт с правами sudo или root
def check_privileges():
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        print(Fore.RED + "ВНИМАНИЕ! Вам нужно запустить этот скрипт с sudo или как root.")
        print(Style.RESET_ALL)
        quit()


# Функция для генерации случайного MAC-адреса
def generate_random_mac_address():
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))

    mac = ""
    for index1 in range(6):
        for index2 in range(2):
            if index2 == 0:
                mac += random.choice(uppercased_hexdigits)
            elif index2 == 1:
                mac += random.choice("02468ACE")
        mac += ":"
    return mac.strip(":")


# Функция для получения текущего MAC-адреса
def get_current_mac():
    output = subprocess.check_output("ip link show", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()


# Функция для определения аргументов argparser
def get_arguments():
    parser = argparse.ArgumentParser(description="Скрипт для изменения MAC-адреса в Linux системах")
    parser.add_argument("-i", "--interface", help="Сетевой интерфейс, MAC-адрес которого будет изменен")
    parser.add_argument("-m", "--mac", help="Новый MAC-адрес, который получит выбранный интерфейс")
    parser.add_argument("-r", "--random", action="store_true", help="Генерирует случайный MAC-адрес")

    args = parser.parse_args()

    # Определяем все доступные сетевые интерфейсы
    avaliable_interfaces = (subprocess.check_output("ip -o link show | awk -F':' '{printf \"%s%s\",sep,$2; sep=\",\"}'", shell=True).decode()).strip().replace(" ", "")
    print("Доступные интерфейсы: " + str(avaliable_interfaces).strip("[]").replace("'", "").replace(",", ", "))
    print("")

    # Создаём список со всеми доступными интерфейсами
    avaliable_interfaces = avaliable_interfaces.split(",")

    # Переменная, используемая для проверки того, был ли уже проверен предоставленный интерфейс
    interface_not_checked = True

    # Обработка значений интерфейса
    while True:
        # Если интерфейс не был определен или его нет в списке "avaliable_interfaces"
        if not args.interface or args.interface not in avaliable_interfaces:
            # Показывать ошибку, только если первое определенное значение интерфейса (полученное из аргумента -i/--interface) недоступно
            if args.interface and interface_not_checked == True:
                print(Fore.RED + f"ОШИБКА! Интерфейс [{args.interface}] недоступен.")
                print(Style.RESET_ALL)
                interface_not_checked = False

            # Запрос ввода имени интерфейса
            args.interface = input("Введите имя интерфейса > ")
            print("")

            # Установить для «interface_not_checked» значение False
            interface_not_checked = False

        # Если предоставленное имя интерфейса находится в списке "avaliable_interfaces"
        if args.interface in avaliable_interfaces:
            print(f"Выбранный интерфейс: [{args.interface}]")
            print("")
            break

        # Если предоставленное имя интерфейса отсутствует в списке "avaliable_interfaces"
        print(Fore.RED + f"ОШИБКА! Интерфейс [{args.interface}] недоступен.")
        print(Style.RESET_ALL)
        print("Доступные интерфейсы: " + str(avaliable_interfaces).strip("[]").replace("'", "").replace(", ", ", "))

    # Обработка значений MAC-адреса
    # Если в качестве аргумента не было передано значение MAC-адреса
    if not args.mac:
        # Если пользователь не указал, хочет ли он случайный MAC-адрес с аргументом "-r/--random"
        if not args.random:
            # Запрашиваем, хочет ли пользователь, чтобы скрипт генерировал случайный MAC-адрес.
            generate_random = input("Вы хотите сгенерировать случайный MAC-адрес?[Y,n] ") or "Y"

        # Если пользователь хочет, чтобы скрипт генерировал случайный MAC-адрес
        if args.random or generate_random.upper() == "Y":
            args.mac = generate_random_mac_address()
            print(f"Случайный MAC-адрес: {args.mac}")

        # Если пользователь не хочет, чтобы скрипт генерировал случайный MAC-адрес
        else:
            while True:
                # Запрос ввода MAC-адреса
                args.mac = input("Введите MAC-адрес > ")

                # Если предоставленный MAC-адрес неверный
                if not re.match(valid_mac_pattern, args.mac):
                    print(Fore.RED + "ОШИБКА! Неверный MAC-адрес.")
                    print(Style.RESET_ALL)

                # Если предоставленный MAC-адрес совпадает с текущим MAC-адресом
                if args.mac.upper() == old_mac.upper():
                    print(Fore.RED + "ОШИБКА! Введенный MAC-адрес совпадает с текущим MAC-адресом.")
                    print(Style.RESET_ALL)

                # Если предоставленный MAC-адрес действителен и не совпадает с текущим MAC-адресом
                if re.match(valid_mac_pattern, args.mac) and not args.mac.upper() == old_mac.upper():
                    break

    return args


# Функция смены MAC-адреса
def change_mac(interface, new_mac):
    print("")
    print(f"Изменение MAC-адреса интерфейса [{interface}] на {new_mac}")

    # Команды для изменения MAC-адреса
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])

    #Обработка изменений
    print("Идёт изменение...")

    for i in tqdm(range(10), bar_format='{percentage}%'):
        sleep(.5)

    # Выводим результаты изменения, а также (старый MAC-адрес и новый MAC-адрес)
    print(Fore.GREEN + "МАС-адрес изменён УСПЕШНО!")
    print(Style.RESET_ALL)
    print(Fore.RED + f"[{interface}] Старый MAC-адрес: {old_mac.upper()}")
    print(Fore.GREEN + f"[{interface}] Новый MAC-адрес: {new_mac}")
    print(Style.RESET_ALL)


# ВЫЗОВЫ ФУНКЦИЙ ПО УМОЛЧАНИЮ
# Проверяем привилегии пользователя
check_privileges()

# Сохранить старый MAC-адрес
old_mac = get_current_mac()

# Аргументы
args = get_arguments()

# Изменить MAC-адрес
change_mac(args.interface, args.mac)
