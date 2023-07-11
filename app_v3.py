from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Настройки подключения к базе данных
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Создаем строку подключения с помощью SQLAlchemy
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Создаем движок SQLAlchemy
engine = create_engine(connection_string)

# Создаем сессию SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Определяем модель данных для таблицы SMSStatus
Base = declarative_base()

class SMSStatus(Base):
    __tablename__ = 'SMSStatus'

    data = Column(DateTime, primary_key=True)
    nomer = Column(String)
    id = Column(Integer)
    status = Column(String)
    body = Column(String)

# Маршрут для обработки запроса и отображения результатов
@app.route('/')
def sms_status():
    # Выполняем запрос к базе данных с помощью SQLAlchemy
    rows = session.query(SMSStatus).order_by(SMSStatus.data.desc()).all()

    # Передаем данные в шаблон Flask для отображения
    return render_template('sms_status.html', rows=rows)

if __name__ == '__main__':
    app.run()
