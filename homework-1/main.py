"""Скрипт для заполнения данными таблиц в БД Postgres."""

import pandas as pd
import psycopg2
from psycopg2 import sql

# Загружаем CSV файлы
employees_df = pd.read_csv("north_data/employees_data.csv")
employees_df = employees_df[["employee_id", "first_name", "last_name", "title", "birth_date", "notes"]]
customers_df = pd.read_csv("north_data/customers_data.csv")
customers_df = customers_df[["customer_id", "company_name", "contact_name"]]
orders_df = pd.read_csv("north_data/orders_data.csv")
orders_df = orders_df[["order_id", "customer_id", "employee_id", "order_date", "ship_city"]]


# Подключаемся к базе данных
connection = psycopg2.connect(
    dbname="north",
    user="postgres",
    password="2428",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()