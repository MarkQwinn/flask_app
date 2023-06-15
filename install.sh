#!/bin/bash

# Проверка наличия python3 и pip в системе
if ! command -v python3 &> /dev/null; then
    echo "Python 3 не найден. Выполняем установку ..."
    # Устанавливаем python3 и pip
    sudo apt update
    sudo apt install -y python3 python3-pip
else
    echo "Python 3 уже установлен"
fi

if ! command -v pip &> /dev/null; then
    echo "pip не найден. Выполняем установку ..."
    # Обновляем pip до последней версии
    sudo -H pip3 install --upgrade pip
else
    echo "pip уже установлен"
fi

# Установка пакета unixodbc
sudo apt-get update
sudo apt-get install unixodbc unixodbc-dev --assume-yes

# Создание виртуального окружения
python3 -m venv myenv
source myenv/bin/activate

# Установка зависимостей из requirements.txt
pip install -r requirements.txt

# Запуск приложения
python main.py
