# - * - coding: utf - 8 -*-
import csv
import xlrd

from app.models import Grade


class FileUtil:
    def __init__(self, myFile):
        self.myFile = myFile

    def dealExcel(self):
        wb = xlrd.open_workbook(filename=None, file_contents=self.myFile)
        table = wb.sheets()[0]
        row = table.nrows
        table_head = ['学号', '姓名', '课程id', '成绩', '补考标记', '缓考标记', '重修标记']
        if row <= 1:
            '''当excel中只有一行或者小于一行时候'''
            return -1;
        else:
            '''判断表头是否与规定表头完全一样'''
            col = table.row_values(0)
            '''长度不一致'''
            if len(col) != len(table_head):
                return -2
            else:
                '''长度一致,检测表头是否完全一致'''
                for i in range(0, len(col)):
                    if col[i] != table_head[i]:
                        '''表头不一致'''
                        return -3
        '''格式正确'''
        '''执行导入操作'''
        grade_info_list = []
        for j in range(1, row):
            stu_id = str(table.row_values(j)[0]).strip("'")
            stu_name = table.row_values(j)[1]
            course_id = table.row_values(j)[2]
            grade = table.row_values(j)[3]
            # make_up_sign = table.row_values(j)[4]
            # re_test_sign = table.row_values(j)[5]
            try:
                grade_info_list.append(Grade(
                    user_name_id=str(stu_id),
                    course_id_id=course_id,
                    grade_value=grade,
                    grade_complain=None
                ))
            except DoesNotExist:
                print("用户不存在")
        try:
            Grade.objects.bulk_create(grade_info_list)
        except e:
            e.prinStact()
            return -4
        # for i in range(1, row):
        #     col = table.row_values(i)
        #     print(col)
        return 0

    def dealCsv(self):
        file_data = self.myFile.decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            fields = line.split(",")
            data_dict = {}
            print(fields[0])
