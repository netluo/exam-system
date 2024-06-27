# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 15:28
# @Author  : chengxiang.luo
# @Email   : zibuyu886@sina.cn
# @File    : db.py
# @Software: PyCharm
import collections

import pymysql


class MysqlConnMgr:
    def __init__(self, user, passwd, host, port, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.myConn = self.mysql_connect()
        self.myCursor = self.mysqlCursor()
        self.qid_range = {}
        self.get_qid_range()

    def mysql_connect(self):
        my_db_conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.passwd,
                                     db=self.db)
        return my_db_conn

    def mysqlCursor(self):
        my_cursor = self.mysql_connect().cursor()
        return my_cursor

    def questionSelect(self, qid):
        self.myCursor.execute("select id, options, isquestion, type from question where id = {id}".format(id=qid))
        question_res = self.myCursor.fetchall()
        return question_res

    def getAnswer(self, qid):
        self.myCursor.execute("select options from answer where id = {id}".format(id=qid))
        answer_res = self.myCursor.fetchall()
        # 返回值形如 (('ABC',),)
        if len(answer_res) > 0:
            return answer_res[0][0]
        else:
            # raise "答案不存在或者题号错误！"
            pass

    def getOptions(self, *args):
        Question = collections.namedtuple('Question', ['id', 'options', 'is_question', 'type'])
        question_dict = {}
        option_list = []
        for i in args[0]:
            question = Question(i[0], i[1], i[2], i[3])
            # 问题类型，分 1,2,3三种，代表单选，多选和判断
            question_dict.update({'type': question.type})
            if question.is_question == 1:
                # 如果是问题放入字典
                question_dict.update({'question': question.options})
            elif question.is_question == 0:
                # 如果是选项，放入选项列表
                option_list.append(question.options)
        # 更新字典数据
        question_dict.update({'options': option_list})
        # question_dict : {'question:': '...', 'options': [... , ... ], 'type' : type -> int}
        return question_dict

    def get_qid_range(self):
        for qtype in range(1, 4):
            self.myCursor.execute(
                f'select min(id), max(id) from question where id > {qtype} * 1000 and id < {qtype + 1} * 1000')
            _res = self.myCursor.fetchall()
            self.qid_range.update({qtype: [_res[0][0], _res[0][1]]})
        print(self.qid_range)

# if __name__ == '__main__':
#     mgr = MysqlConnMgr('lcx', 'root123', '192.168.32.128', 3306, 'examine')
#     _res = mgr.questionSelect(2001)
#     mgr.getOptions(_res)
