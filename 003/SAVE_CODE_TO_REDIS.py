# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2016-11-27 10:57:37
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-03-02 19:42:56

import string
import random
import redis


NUMBER_OF_CODE_TO_GENERATE = 200
POPULATION = string.letters + string.digits


def generate_code(length=16):
    result = ''
    for i in range(length):
        if i and i % 4 == 0:
            result += '-'
        result += str(random.choice(POPULATION))
    return result


def get_redis_conn():
    return redis.Redis(host='localhost', port=6379, db=0)


def vatification():
    codes = get_redis_conn().lrange('code', 0, -1)
    for code in codes:
        print code


if __name__ == '__main__':
    r = get_redis_conn()
    for i in range(NUMBER_OF_CODE_TO_GENERATE):
        r.lpush('code', generate_code())
    vatification()
