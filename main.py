from flask import Flask
import pandas as pd
import pyodbc

app = Flask(__name__)

# Устанавливаем параметры подключения к базе данных
server = 'SERVER'
database = 'DATABASE'
username = 'LOGIN'	
password = 'PASSWORD'


def get_data_from_database():
    try:
        # Подключаемся к базе данных
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=' + server + ';'
                                    'DATABASE=' + database + ';'
                                    'UID=' + username + ';'
                                    'PWD=' + password + ';')

        # Выполняем SQL-запрос и получаем результаты в DataFrame
        query = "SELECT * FROM таблица"
        df = pd.read_sql_query(query, connection)

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
        # Фильтруем данные по определенному условию
        filtered_df = df[df['Age'] > 25]

        # Преобразуем данные в формат JSON
        json_data = filtered_df.to_json(orient='records')

        return json_data

    else:
        return "Ошибка при получении данных из базы данных"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
