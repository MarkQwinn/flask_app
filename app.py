from flask import Flask
import pyodbc

app = Flask(__name__)

# Настройки подключения к базе данных
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Маршрут Flask-приложения
@app.route('/smsstatus')
def get_sms_status():
    try:
        # Создание соединения с базой данных
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        
        # Создание курсора для выполнения запросов
        cursor = conn.cursor()

        # Выполнение запроса
        cursor.execute("SELECT [data], [nomer], [id], [status], [body] FROM [dbo].[SMSStatus] ORDER BY [data] DESC")

        # Получение результатов запроса
        results = cursor.fetchall()

        # Форматирование результатов в удобный вид (например, возвращение JSON)
        formatted_results = []
        for row in results:
            formatted_results.append({
                'data': row.data,
                'nomer': row.nomer,
                'id': row.id,
                'status': row.status,
                'body': row.body
            })

        # Закрытие курсора и соединения
        cursor.close()
        conn.close()

        # Возврат результатов в формате JSON
        return {'sms_status': formatted_results}

    except Exception as e:
        # Обработка ошибок при выполнении запроса
        return {'error': str(e)}

if __name__ == '__main__':
    app.run()
