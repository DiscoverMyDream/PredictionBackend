# -*- coding: utf-8 -*-
import sys
from pycel import ExcelCompiler

filename = "CPGAtoGPA.xlsx"
excel = ExcelCompiler(filename=filename)
excel.evaluate('Sheet1!F2')
excel.set_value('Sheet1!F2', 10)
excel.evaluate('Sheet1!H2')
excel.evaluate('Sheet1!F2')
excel.evaluate('Sheet1!H3')

CGPA=float(sys.argv[1])

excel.set_value('Sheet1!F2', CGPA)
GPA=excel.evaluate('Sheet1!H2')
GPA=round(float(GPA),2)
print(GPA)
Grade=excel.evaluate('Sheet1!H3')
print(Grade)


