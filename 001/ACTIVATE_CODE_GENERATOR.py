# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-11-08 15:35:35
# @Last Modified by:   rhys
# @Last Modified time: 2016-11-08 18:11:21

import random, string

POPULATION = string.letters + string.digits


def generate_code(length = 16):
	result = ''
	for i in range(length):
		if i and i % 4 == 0:
			result += '-'
		result += str(random.choice(POPULATION))
	return result


if __name__ == '__main__':
	with open('Activate_code.txt', 'w+') as f:
		for i in range(200):
			 f.write(generate_code(32) + '\n')