#!/bin/bash

# Проверяем, активировано ли виртуальное окружение
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Виртуальное окружение не активировано"
  # Активируем виртуальное окружение
  source myenv/bin/activate
fi

# Запускаем приложение
python main.py
