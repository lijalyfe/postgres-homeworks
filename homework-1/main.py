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


# Вспомогательная функция для создания SQL-запроса на основе DataFrame
def create_insert_query(table_name, df):
    column_names = ", ".join(df.columns)
    q = sql.SQL(
        f"INSERT INTO {table_name} ({column_names})"
        " VALUES ({})"
    )
    return q


# Заполняем таблицу employees данными
for _, row in employees_df.iterrows():
    query = create_insert_query("employees", employees_df).format(
        sql.SQL(", ").join(sql.Placeholder() for _ in row)
    )
    cursor.execute(query, tuple(row))

# Заполняем таблицу customers данными
for _, row in customers_df.iterrows():
    query = create_insert_query("customers", customers_df).format(
        sql.SQL(", ").join(sql.Placeholder() for _ in row)
    )
    cursor.execute(query, tuple(row))

# Заполняем таблицу orders данными
for _, row in orders_df.iterrows():
    query = create_insert_query("orders", orders_df).format(
        sql.SQL(", ").join(sql.Placeholder() for _ in row)
    )
    cursor.execute(query, tuple(row))


# Завершаем транзакцию
connection.commit()

# Закрываем курсор и соединение с базой данных
cursor.close()
connection.close()
