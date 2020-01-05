#!/usr/bin/env python3
import uuid
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Users(Base):
	"""Описывает структуру таблицы athletes для хранения записей"""
	__tablename__ = "user"
	id = sa.Column(sa.INTEGER, primary_key=True)
	birthdate = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	
	
engine = sa.create_engine(DB_PATH)
# создаем фабрику сессию
Sessions = sessionmaker(engine)
# cоздаем сессию

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Привет! Программа найдёт похожего на вас спортсмена")
    ("Пожалуйста, впишите ваши данные")
    # запрашиваем у пользователя данные
    first_name = input("Ваше имя: ")
    last_name = input("фамилия: ")
    birthdate = input("дата рождения(год-месяц-день)")
    gender = input("ваш пол ( Male / Female )" )
    height = input("Рост (метры.сантиметры) ")
    email = input("e-mail: ")
    # генерируем идентификатор пользователя и сохраняем его строковое представление
    user_id = str(uuid.uuid4())
    # создаем нового пользователя
    user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name,
        gender = gender,
        birthdate = birthdate,
        height = height,
        email=email
    )
    # возвращаем созданного пользователя
    return user

def main():
	session = Sessions()

	users = session.query(Users).all()


if __name__ == "__main__":
    main()