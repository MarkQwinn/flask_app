#!/bin/bash

# Создание виртуального окружения
python3 -m venv myenv
source myenv/bin/activate

# Установка зависимостей из requirements.txt
pip install -r requirements.txt

# Установка пакета unixodbc
sudo apt-get update
sudo apt-get install unixodbc unixodbc-dev --assume-yes

# Запуск приложения на Python
python main.py
