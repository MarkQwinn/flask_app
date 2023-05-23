from config import LOGIN
from config import PASSWORD
from flask import Flask, jsonify
import pandas as pd
import pyodbc

app = Flask(__name__)

# Устанавливаем параметры подключения к базе данных
server = '127.0.0.1'
database = 'MyDatebase'
username = LOGIN	
password = PASSWORD


def get_data_from_database():
    try:
        # Подключаемся к базе данных
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=' + server + ';'
                                    'DATABASE=' + database + ';'
                                    'UID=' + username + ';'
                                    'PWD=' + password + ';')

        # Создаем курсор для выполнения SQL-запросов
        cursor = connection.cursor()

        # Выполняем SQL-запрос
        query = "SELECT * FROM таблица"
        cursor.execute(query)

        # Получаем результаты запроса
        results = cursor.fetchall()

        # Закрываем курсор и соединение с базой данных
        cursor.close()
        connection.close()

        return results

    except pyodbc.Error as err:
        print("Ошибка при подключении к базе данных: {}".format(err))
        return None


@app.route('/')
def index():
    # Получаем данные из базы данных
    data = get_data_from_database()

    if data:
        # Фильтруем данные по определенному условию
        filtered_data = [row for row in data if row[2] > 25]

        # Преобразуем данные в формат JSON
        json_data = jsonify(filtered_data)

        return json_data

    else:
        return "Ошибка при получении данных из базы данных"


if __name__ == '__main__':
    app.run()
