import os

from pdf2docx import Converter

import ui_路径选择 as pick


def trans(file: str, desktop: str) -> None:
	# 获取文件名称
	file_name = file.split('.')[0]
	# pdf文件名称
	pdf_name = file
	# docx文件名称
	docx_name = file_name + '.docx'
	# 加载pdf文档
	try:
		cv = Converter(pdf_name)
		cv.convert(docx_name, start = 0, end = None)
	except AttributeError:
		input("转换失败！")


def choose() -> None:
	desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
	name = pick.QFileDialog.getOpenFileName(
		None,  # 父窗口对象
		"选择你要上传的图片",  # 标题
		desktop,  # 起始目录
		"可携带文档格式 (*.pdf)"  # 选择类型过滤项，过滤内容在括号中
	)
	ui.label.setText(name[0])
	trans(name[0], desktop)


app = pick.QApplication([])
MainWindow = pick.QWidget()
# MainWindow.move(0, 0)  # 定义初始位置
ui = pick.Ui_Form()
ui.setupUi(MainWindow)
ui.pushButton.clicked.connect(choose)
MainWindow.show()
app.exec()
