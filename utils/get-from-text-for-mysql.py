# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 11:51
# @Author  : chengxiang.luo
# @Email   : zibuyu886@sina.cn
# @File    : get-from-text-for-mysql.py
# @Software: PyCharm
import argparse
import re

import pymysql


class ReadFromTXT:
    def __init__(self, file_name):
        self.option_type = 1
        self.begin_id = 0
        self.file = file_name
        self.conn = pymysql.connect(host='192.168.32.128', port=3306, user='lcx', passwd='root123', db='mysqlexamine',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def insert_to_question(self, id, options, is_question, qtype):
        self.cursor.execute(
            'insert into question values (%d,"%s", %d, %d)' % (id, options, is_question, qtype))
        self.conn.commit()

    def insert_to_answer(self, id, options):
        self.cursor.execute('insert into answer values (%d, "%s")' % (id, options))
        self.conn.commit()

    def judge_answer(self):
        questions = ''
        answer = ''
        with open(self.file, mode='r', encoding='utf8') as qfile:
            lines = qfile.readlines()
            self.begin_id = 1001
            for line in lines:
                if re.match('[A-H]、', line.strip()):
                    # options = options + '\n' + line.strip()
                    self.insert_to_question(self.begin_id, line.strip().lstrip('[A|B|C|D|E|F|G|H|I|J|K]、').strip(), 0,
                                            1)
                    pass

                elif re.match('Answer', line.strip()):
                    # type :
                    # 1 : 单选
                    # 2 : 多选
                    # 3 : 判断
                    options = line.split(':')[-1].strip()
                    self.insert_to_answer(self.begin_id, options)
                    self.insert_to_question(self.begin_id, questions, 1, 1)
                    if len(options) > 1:
                        self.cursor.execute(f"update question set type = 2 where id = {self.begin_id}")
                        self.conn.commit()

                    # 遇到'Answer' 的时候，表示这个问题结束了，开始清空question，自增
                    questions = ''
                    self.begin_id += 1
                else:
                    questions = questions + '\n' + line.strip()


if __name__ == '__main__':
    myparser = argparse.ArgumentParser()
    myparser.add_argument('--file', '-f', help='set the file name', required=True)
    args = myparser.parse_args()
    file_name = args.file
    # username = args.user
    if args.file:
        ReadFromTXT(file_name).judge_answer()
