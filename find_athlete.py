#!/usr/bin/env python3
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from users import Users

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()
engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()


class Athletes(Base):
	"""Описывает структуру таблицы athletes для хранения записей."""
	__tablename__ = "athelete"
	id = sa.Column(sa.INTEGER, primary_key=True)
	age = sa.Column(sa.INTEGER)
	birthdate = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)
	name = sa.Column(sa.TEXT)
	weight = sa.Column(sa.TEXT)
	gold_medals = sa.Column(sa.INTEGER)
	silver_medals = sa.Column(sa.INTEGER)
	bronze_medals = sa.Column(sa.INTEGER)
	total_medals = sa.Column(sa.INTEGER)
	sport = sa.Column(sa.TEXT)
	country = sa.Column(sa.TEXT)


def user_input():
	"""Запрашивает ID у пользователя и возвращает ID"""
	user_table = session.query(Users).all()
	print()
	print("Программа найдет ближайших к вам атлетов по росту и дате рождения ")
	user_id = input("Введите ваш ID: ")
	if int(user_id) > len(user_table):
		print("такого ID не существует")
		exit()
	else:
		return user_id


def find_height_atlet(user_id):
	"""Находит по ID пользователя, ближайшего к нему атлета по росту, выводит сообщение"""
	query_users = session.query(Users.height).filter(Users.id == user_id)
	user_height = round(query_users[0][0], 2)
	print()
	print("Ваш рост", user_height)
	print()
	equal_atlet = session.query(Athletes).filter(Athletes.height == user_height).first()
	lower_atlet = session.query(Athletes).filter(Athletes.height < user_height).first()
	highter_atlet = session.query(Athletes).filter(Athletes.height > user_height).first()
	if equal_atlet is not None:
		print(equal_atlet.name, "одного с вами роста", equal_atlet.height, "Вид спорта", equal_atlet.sport)

	elif lower_atlet is None:
		print("Ближайший по росту атлет: ", highter_atlet.name, highter_atlet.height, "Вид спорта", highter_atlet.sport)

	elif highter_atlet is None:
		print("Ближайший по росту атлет: ", lower_atlet.name, lower_atlet.height, "Вид спорта", lower_atlet.sport)

	elif (highter_atlet.height - user_height) > (user_height - lower_atlet.height):
		print("Ближайший по росту атлет: ", lower_atlet.name, lower_atlet.height, "Вид спорта", lower_atlet.sport)

	else:
		print("Ближайший по росту атлет: ", highter_atlet.name, highter_atlet.height, "Вид спорта", highter_atlet.sport)


def find_bithday_atlet(user_id):
	"""Находит по ID пользователя, ближайшего к нему атлета по дате рождения, выводит сообщение."""
	query_users = session.query(Users.birthdate).filter(Users.id == user_id)
	user_birthdate_str = query_users[0][0]
	user_birthdate = datetime.datetime.strptime(user_birthdate_str, "%Y-%m-%d").date()
	print()
	print("Ваша дата рождения :", user_birthdate)
	query = session.query(Athletes).all()
	atlets_birthdays = [Athletes.birthdate for Athletes in query]
	start_delta = datetime.timedelta(days = 1000000, hours = 0, minutes = 0)
	list_birthday_atlet = []
	for item in atlets_birthdays:
		birthdate_time = datetime.datetime.strptime(item, "%Y-%m-%d").date()
		min_delta = abs(birthdate_time - user_birthdate)
		if min_delta < start_delta:
		 	list_birthday_atlet.append(item)
		 	start_delta = min_delta
	result_birthday_atlet = list_birthday_atlet[-1]
	result_atlet = session.query(Athletes).filter(Athletes.birthdate == result_birthday_atlet).first()
	print()
	print("Ближайший по дате рождения атлет: ")
	print(result_atlet.name, result_atlet.birthdate, "Вид спорта", result_atlet.sport)


def main():
	user_id = user_input()
	find_bithday_atlet(user_id)
	find_height_atlet(user_id)
	
if __name__ == "__main__":
	main()
