#!/usr/bin/env python3
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Users(Base):
    """Описывает структуру таблицы athletes для хранения записей"""
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    email = sa.Column(sa.Text)


def __str__(self):
		return self.first_name
	
def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Программа найдёт похожего на вас спортсмена")
    print("Пожалуйста, впишите ваши данные")
    # запрашиваем у пользователя данные
    first_name = input("Ваше имя: ")
    last_name = input("фамилия: ")
    birthdate = input("дата рождения(год-месяц-день)")
    gender = input("ваш пол ( Male / Female )" )
    height = input("Рост (метры.сантиметры) ")
    email = input("e-mail: ")
      # создаем нового пользователя
    user = Users(
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
	engine = sa.create_engine(DB_PATH)
	Sessions = sessionmaker(engine)
	session = Sessions()
	user = request_data()
	session.add(user)
	session.commit()
	print("Ваш ID: ", user.id)


if __name__ == "__main__":
	main()
