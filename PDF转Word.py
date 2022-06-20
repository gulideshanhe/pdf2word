import os
from pdf2docx import Converter

file = input("输入文件名:") + ".pdf"
# 获取文件名称
file_name = file.split('.')[0]
# pdf文件名称
pdf_name = os.getcwd() + '\\' + file
# docx文件名称
docx_name = os.getcwd() + '\\' + file_name + '.docx'
# 加载pdf文档
try:
	cv = Converter(pdf_name)
	cv.convert(docx_name, start = 0, end = None)
except AttributeError:
	input("转换失败！")
