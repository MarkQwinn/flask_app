from flask import Flask
import pandas as pd
import pyodbc
import configparser

app = Flask(__name__)

# Загружаем параметры из файла конфигурации
config = configparser.ConfigParser()
config.read('config.ini')

# Получаем параметры подключения к базе данных из файла конфигурации
server = config.get('database', 'server')
database = config.get('database', 'database')
username = config.get('database', 'username')
password = config.get('database', 'password')

# Получаем SQL-запрос и условие фильтрации из файла конфигурации
sql_query = config.get('query', 'sql_query')


def get_data_from_database():
    try:
        # Подключаемся к базе данных
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=' + server + ';'
                                    'DATABASE=' + database + ';'
                                    'UID=' + username + ';'
                                    'PWD=' + password + ';')

        # Выполняем SQL-запрос и получаем результаты в DataFrame
        df = pd.read_sql_query(sql_query, connection)

        # Закрываем соединение с базой данных
        connection.close()

        return df

    except pyodbc.Error as err:
        print("Ошибка при подключении к базе данных: {}".format(err))
        return None


@app.route('/')
def index():
    # Получаем данные из базы данных
    df = get_data_from_database()

    if df is not None:
        # Преобразуем данные в формат JSON
        json_data = df.to_json(orient='records')

        return json_data

    else:
        return "Ошибка при получении данных из базы данных"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
