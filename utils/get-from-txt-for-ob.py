# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 15:14
# @Author  : chengxiang.luo
# @Email   : zibuyu886@sina.cn
# @File    : get-from-txt-for-ob.py
# @Software: PyCharm

import argparse

import pymysql


class ReadFromTXT:
    def __init__(self, file_name, qtype):
        self.option_type = 1
        self.begin_id = 0
        self.file = file_name
        self.qtype = qtype
        self.conn = pymysql.connect(host='192.168.32.128', port=3306, user='lcx', passwd='root123', db='examine',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def insert_to_question(self, id, options, is_question, question_type):
        self.cursor.execute(
            'insert into question values (%d, "%s", %d, %d)' % (id, options, is_question, question_type))
        self.conn.commit()

    def insert_to_answer(self, id, options):
        self.cursor.execute('insert into answer values (%d, "%s")' % (id, options))
        self.conn.commit()

    def write_to_db(self):
        print(self.qtype, self.file)
        if self.qtype == 1:
            self.begin_id = 1001
        elif self.qtype == 2:
            self.begin_id = 2001
        else:
            self.begin_id = 3001
        with open(self.file, mode='r', encoding='utf8') as qfile:
            lines = qfile.readlines()
            for line in lines:
                print(line)
                if line.strip() == '':
                    self.begin_id += 1
                    self.option_type = 1
                    continue
                elif '答案' in line:
                    self.insert_to_answer(self.begin_id, line.split('：')[-1].strip())
                    line.split('：')[-1].strip()
                # elif ('？' in line) or ('?' in line) or ('单选' in line):
                else:
                    line = line.lstrip('A、').lstrip('B、').lstrip('C、').lstrip('D、').lstrip('E、').lstrip('F、').lstrip(
                        'G、').strip()
                    self.insert_to_question(self.begin_id, line, self.option_type, self.qtype)
                    self.option_type = 0
                # elif '答案' in line:
                #     line
                #     line = line.lstrip('A、').lstrip('B、').lstrip('C、').lstrip('D、').strip()


if __name__ == '__main__':
    myparser = argparse.ArgumentParser()
    myparser.add_argument('--version', help='print the version', action='store_true')
    myparser.add_argument('--file', '-f', help='set the file name', required=True)
    myparser.add_argument('--qtype', '-t', type=int, help='set the question type', required=True)
    args = myparser.parse_args()
    file_name = args.file
    qtype = args.qtype
    # username = args.user
    if args.file and args.qtype:
        ReadFromTXT(file_name, qtype).write_to_db()
