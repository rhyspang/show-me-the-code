# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-11-08 18:10:10
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-11-27 12:05:30


import MySQLdb
import string
import random

POPULATION = string.letters + string.digits
URL = 'localhost'
USER = 'root'
PASSWORD = 'sefd'
DB_NAME = 'python_test_show_me_the_code'
TB_NAME = 'activate_code'
NUMBER_OF_CODE_TO_GENERATE = 200

CREATE_DB_SQL = "CREATE DATABASE IF NOT EXISTS %s" % DB_NAME
USER_DB_SQL = "USE %s" % DB_NAME
CREATE_TB_SQL 	=  "CREATE TABLE IF NOT EXISTS "     \
    "%s(id INT PRIMARY KEY AUTO_INCREMENT, code VARCHAR(52))" % TB_NAME
INSERT_TB_SQL = r"INSERT %s(code) VALUES" % TB_NAME


def generate_code(length=16):
    result = ''
    for i in range(length):
        if i and i % 4 == 0:
            result += '-'
        result += str(random.choice(POPULATION))
    return result


if __name__ == '__main__':
    conn = MySQLdb.connect(URL, USER, PASSWORD)
    cur = conn.cursor()
    cur.execute(CREATE_DB_SQL)
    cur.execute(USER_DB_SQL)
    cur.execute(CREATE_TB_SQL)
    for i in range(NUMBER_OF_CODE_TO_GENERATE):
        try:
            cur.execute(INSERT_TB_SQL+"('%s')" % generate_code())
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e

    conn.close()
