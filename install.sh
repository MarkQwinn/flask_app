#!/bin/bash

# Установка python3, python3-pip, unixodbc
sudo apt update
sudo apt install -y python3 python3-pip unixodbc unixodbc-dev

# Обновление pip
sudo -H pip3 install --upgrade pip

# Создание виртуального окружения
python3 -m venv myenv
source myenv/bin/activate

# Установка зависимостей из requirements.txt
pip install -r requirements.txt

# Запуск приложения
python main.py
