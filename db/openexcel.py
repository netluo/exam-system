# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 15:40
# @Author  : chengxiang.luo
# @Email   : zibuyu886@sina.cn
# @File    : openexcel.py
# @Software: PyCharm

import pandas as pd
from sqlalchemy import create_engine


class ManExcel:
    def __init__(self, filename, sheet_cnt):
        self.filename = filename
        self.sheet_cnt = sheet_cnt
        self.exam_dict = {}

    def readExcel(self):
        engine = create_engine("mysql://lcx:root123@192.168.32.128/examine",
                               encoding='utf8', echo=True)
        for i in range(self.sheet_cnt):
            all_sheets = pd.DataFrame(pd.read_excel(self.filename, sheet_name=i))
            all_sheets = all_sheets.set_index('id')
            all_sheets.to_sql('question', con=engine, if_exists='append')


if __name__ == '__main__':
    ManExcel('../题.xlsx', 3).readExcel()
