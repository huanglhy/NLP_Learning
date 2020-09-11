# -*- coding: utf-8 -*-
import xlrd


class readFromExcel():
    def __init__(self, filepath):
        self.filepath = filepath
        self.answerDict = {}
        self.DataStrut = {}
        self.query2row = {}

    @staticmethod
    def strQ2B(ustring):
        """全角转半角"""
        rstring = ""
        for uchar in ustring:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248

            rstring += chr(inside_code)
        return rstring

    @staticmethod
    def lowercase(ustring):
        """大写转小写"""
        return ustring.lower()

    @staticmethod
    def titlecase(ustring):
        """转书写格式"""
        return ustring.title()


    def load_excel(self):
        tableOp = xlrd.open_workbook(self.filepath)
        sheetFrame = tableOp.sheet_by_index(0)

        self.arange_Strut(sheetFrame)


    def arange_Strut(self, sheet):
        readCount = 0
        readIndex = 0

        for row in range(1, sheet.nrows):
            read_flag = False

            # 问题
            row_query, row_similar, row_ans = sheet.row_values(row)


            if len(row_query) < 3:
                not_short_flag = False
                print('Too short')
            else:
                not_short_flag = True

            if row_ans and row_query and not_short_flag:
                if self.lowercase(self.strQ2B(row_query)) in self.DataStrut: # BUG: simply remove repeat
                    print('repeat')
                    read_flag = True
                else:
                    self.answerDict[row - 1] = self.lowercase(self.strQ2B(row_ans.strip()))
                    self.DataStrut[self.lowercase(self.strQ2B(row_query))] = row - 1
                    self.query2row[readIndex] = row - 1

                    readIndex += 1
                    read_flag = True


            #相似问题
            if row_similar:
                read_flag = True
                for sub_query in row_similar.split('\n'):
                    if len(sub_query) < 3:
                        continue
                    if self.lowercase(self.strQ2B(sub_query)) in self.DataStrut:
                        print('repeat')
                        continue
                    self.answerDict[row - 1] = self.lowercase(self.strQ2B(row_ans.strip()))

                    self.DataStrut[self.lowercase(self.strQ2B(sub_query))] = row - 1
                    self.query2row[readIndex] = row - 1

                    readIndex += 1
            if read_flag:
                readCount += 1

        print('All read lines:\t{readCount}')


if __name__ == '__main__':
    a = readFromExcel(filepath=r'D:\pycharm_project\knowledge_rule\datas\question_base.xlsx')
    a.load_excel()
    print(a.DataStrut)
    print(a.answerDict)
