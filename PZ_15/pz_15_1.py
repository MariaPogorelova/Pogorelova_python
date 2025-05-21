# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).
import sqlite3 as sq
with sq.connect('test.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users 
    (user_id integer primary key autoincrement,
    name text not null,
    sex integer not null default 1,
    old integer,
    score integer)""")