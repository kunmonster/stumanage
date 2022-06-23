# - * - coding: utf - 8 -*-
import csv

class FileUtil:
    def __init__(self, myFile):
        self.myFile = myFile
    def dealExcel(self):
        return ''
    def dealCsv(self):
        header_row = next(self.myFile)
        print(header_row)