import datetime
import random
import string
from collections import namedtuple

import pymysql.cursors
from typing import Optional

db_config: dict = {
    'host': 'localhost',
    'user': 'root',
    'password': 'kjhlkjhl',
    'database': 'at_sea_chat_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
digit_of_token_bits = 32  # token 为 32 位，at_sea_chat_db 数据库的 token 表的 token 字段亦为 32 位

def _insert(sql: str, args: tuple) -> None:
    connection = pymysql.connect(**db_config)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, args)
        connection.commit()

def _selcet_one(sql: str, args: tuple) -> Optional[dict]:
    connection = pymysql.connect(**db_config)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, args)
            result = cursor.fetchone()
            return result


def add_user(user: str, password: str, email: str) -> namedtuple('Status', ['isOk', 'massage']):
    pass