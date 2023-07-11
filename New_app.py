from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Настройки подключения к базе данных
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'

# Маршрут для обработки запроса и отображения результатов
@app.route('/')
def sms_status():
    # Устанавливаем соединение с базой данных
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server +
                          ';DATABASE=' + database + ';UID=' + username +
                          ';PWD=' + password)

    # Создаем курсор для выполнения запроса
    cursor = conn.cursor()

    # Выполняем запрос к базе данных
    query = '''
        SELECT [data], [nomer], [id], [status], [body]
        FROM [dbo].[SMSStatus]
        ORDER BY [data] DESC
    '''
    cursor.execute(query)

    # Получаем все строки результата
    rows = cursor.fetchall()

    # Закрываем курсор и соединение с базой данных
    cursor.close()
    conn.close()

    # Передаем данные в шаблон Flask для отображения
    return render_template('sms_status.html', rows=rows)

if __name__ == '__main__':
    app.run()
