import datetime
import random
import string

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


def _selcet_one(sql: str, args: tuple) -> Optional[dict[str, str]]:
    connection = pymysql.connect(**db_config)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, args)
            result = cursor.fetchone()
            return result


def add_user(user_name: str, password: str, email: str) -> dict[str, str]:
    status = {"isOK": "False",
              'massage': 'it is more than 255 characters the user_name or password or email '
                         'contains'}
    if len(user_name) > 255 or len(password) > 255 or len(email) > 255:
        return status
    if select_user(user_name) is not None:
        status['massage'] = f'the user {user_name} already exists'
        return status

    sql: str = "INSERT INTO `user` (username, password, email) VALUE (%s, %s, %s)"
    args: tuple = (user_name, password, email)
    _insert(sql, args)
    status['isOk'] = 'True'
    status['massage'] = f'successfully create the user {user_name}'
    return status


def select_user(username: str) -> Optional[dict[str, str]]:
    sql: str = "SELECT `userid`, `username`, `password`, `email` FROM `user` WHERE `username` = %s"
    args: tuple[str] = (username,)
    return _selcet_one(sql, args)


def _select_token_by_token(token: str) -> dict[str: str, str: int, str: datetime.datetime]:
    sql = 'SELECT `token`, `userid`, `create_date` FROM token WHERE token = %s'
    args: tuple = (token,)
    return _selcet_one(sql, args)


def _insert_token(userid: int) -> dict[str: Optional[str]]:
    status = {'isInsert': True,
              'token': None,
              'massage': 'successfully insert token'}
    # 如果新 token 与 数据库中的 token 重复，再生成个新 token，直到插入成功。当然，最多生成 5 次
    for _ in range(5):
        status['token'] = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        if _select_token_by_token(status['token']) is None:
            sql = 'INSERT INTO token (token, userid) VALUE (%s, %s)'
            args: tuple = (status['token'], userid)
            _insert(sql, args)
            return status
        else:
            continue

    status['isInsert'] = False
    status['massage'] = "Five consecutive tokens have been generated that duplicate existing tokens in the database. " \
                        "You are a fucking chosen one. Maybe is time to reconstruct your code and database!!!"
    return status


def login(username: str, password: str) -> dict[str: Optional[str]]:
    status = {'isOk': 'False',
              'massage': 'the user name dose not exist',
              'token': None}
    user_info: Optional[dict[str, str]] = select_user(username)
    if user_info is None:
        return status
    if user_info['password'] != password:
        status['massage'] = 'the user password is incorrect'
        return status

    token_info = _insert_token(user_info['userid'])
    if token_info['isInsert']:
        status['isOk'] = 'True'
        status['massage'] = 'successfully login'
        status['token'] = token_info['token']
        return status
    else:
        status['massage'] = token_info['massage']
        return status


def correct_token(userid: int, token: str) -> dict[str: str]:
    status = {'isActive': 'False',
              'massage': 'token dose note exist'}
    token_info = _select_token_by_token(token)
    if token_info is None:
        return status
    if token_info['userid'] != userid:
        status['massage'] = 'the token dose not match the userid'
        return status
    status['isActive'] = 'True'
    status['massage'] = 'this is a correct token'
    return status


if __name__ == '__main__':
    print(add_user('add_user', 'passwd', 'e@e.com'))
    print(select_user('add_user'))
    print(type(select_user('add_user')))
    print(select_user('add_user').get('password') == 'passwd')
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    print(type(ran_str))
    print(login('testuser', 'testpassword'))
    print(correct_token(1, '11111111111111111111111111111111'))
