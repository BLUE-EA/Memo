# python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os,time

class Memo(QWidget):
    def __init__(self):
        super().__init__()
        self.time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        # 日历部分的布局
        self.cal_widget = QWidget()
        self.cal_widget.setObjectName("cal_widget")
        self.cal_layout = QGridLayout()
        self.cal_widget.setLayout(self.cal_layout)

        # textbox部分的布局
        self.textbox_widget = QWidget()
        self.textbox_widget.setObjectName("textbox_widget")
        self.textbox_layout = QVBoxLayout()
        self.textbox_widget.setLayout(self.textbox_layout)

        self.main_layout.addWidget(self.cal_widget,0,0)
        self.main_layout.addWidget(self.textbox_widget,1,0)

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.setMinimumDate(QDate(1988, 1, 1))  # 设置日历的最大最小日期
        self.cal.setMaximumDate(QDate(2088, 1, 1))
        self.cal.clicked.connect(self.get_time)
        self.main_layout.addWidget(self.cal, 0, 0)

        self.tool_widget = QWidget()
        self.tool_layout = QHBoxLayout()
        self.tool_widget.setLayout(self.tool_layout)
        self.textbox_layout.addWidget(self.tool_widget)

        self.label = QLabel(self)
        self.label.setText(self.time)
        self.tool_layout.addWidget(self.label)

        self.setting_btn = QPushButton(self)
        self.setting_btn.setObjectName('button')
        self.setting_btn.setText("")
        self.tool_layout.addWidget(self.setting_btn)

        self.save_btn = QPushButton(self)
        self.save_btn.setObjectName('button')
        self.save_btn.setText("保存")
        self.save_btn.resize(20, 20)
        self.save_btn.clicked.connect(self.save_file)
        self.tool_layout.addWidget(self.save_btn)

        self.extend_btn = QPushButton(self)
        self.extend_btn.setObjectName('button')
        self.extend_btn.setText("关闭日历")
        self.extend_btn.clicked.connect(self.smaller)
        self.tool_layout.addWidget(self.extend_btn)


        self.label.setStyleSheet('''
                                    QLabel{
                                        color: white;    
                                    }
                                ''')

        self.save_btn.setStyleSheet('''
                                        QPushButton{
                                            border:none;
                                            color:white;
                                        }
                                        QPushButton#button{
                                            border:none;
                                            font-size:18px;
                                            font-weight:700;
                                            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                        }
                                        QPushButton#button:hover{
                                            font-weight:700;
                                            border-bottom: 3px solid white;
                                        }
                                    ''')

        self.setting_btn.setStyleSheet('''
                                                QPushButton{
                                                    border:none;
                                                    color:white;
                                                }
                                            ''')

        self.extend_btn.setStyleSheet('''
                                        QPushButton{
                                                border:none;
                                                color:white;
                                            }
                                            QPushButton#button{
                                                border:none;
                                                font-size:14px;
                                                font-weight:100;
                                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                            }
                                            QPushButton#button:hover{
                                                font-weight:700;
                                            }    
                                    ''')

        self.textbox = QTextEdit(self)
        self.textbox.resize(200, 300)
        task = self.open_file(self.time)
        if task:
            self.textbox.setText(task)
        else:
            self.textbox.setText("今天什么任务都没有哦~")
        self.textbox_layout.addWidget(self.textbox)

        self.main_layout.setSpacing(0)

        self.setGeometry(1200, 300, 300, 220)
        self.setWindowTitle('备忘录')
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setMinimumSize(350, 550)
        self.setMaximumSize(350, 550)
        self.setWindowIcon(QIcon('title.jfif'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.show()


    def get_time(self, date):
        self.time = date.toString("yyyy-MM-dd")
        self.label.setText(self.time)
        task = self.open_file(self.time)
        if task:
            self.textbox.setText(task)
        else:
            self.textbox.setText("今天什么任务都没有哦~")


    def open_file(self,title):
        if os.path.exists('./Note/'+title):
            with open('./Note/' + title, 'r', encoding="utf-8") as f:
                return f.read()
        else:
            return '今天什么任务都没有哦~'

    def save_file(self):
        new_task = self.textbox.toPlainText()
        with open('./Note/'+self.time, 'w', encoding='utf-8') as file_object:
            file_object.write(new_task)

    def smaller(self):
        self.hide()
        self.objectMemo = SimpleMemo()
        self.objectMemo.show()


class SimpleMemo(QWidget):
    def __init__(self):
        super().__init__()
        self.time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        # 日历部分的布局
        self.cal_widget = QWidget()
        self.cal_widget.setObjectName("cal_widget")
        self.cal_layout = QGridLayout()
        self.cal_widget.setLayout(self.cal_layout)

        # textbox部分的布局
        self.textbox_widget = QWidget()
        self.textbox_widget.setObjectName("textbox_widget")
        self.textbox_layout = QVBoxLayout()
        self.textbox_widget.setLayout(self.textbox_layout)

        self.main_layout.addWidget(self.cal_widget,0,0)
        self.main_layout.addWidget(self.textbox_widget,1,0)

        self.up_label = QLabel()
        self.up_label.setText('加油吧，少年，你还有好多任务没有完成呢！')
        self.main_layout.addWidget(self.up_label, 0, 0)

        self.up_label.setStyleSheet('''
                                    QLabel{
                                        color: white;    
                                    }
                                ''')

        self.tool_widget = QWidget()
        self.tool_layout = QHBoxLayout()
        self.tool_widget.setLayout(self.tool_layout)
        self.textbox_layout.addWidget(self.tool_widget)

        self.label = QLabel(self)
        self.label.setText(self.time)
        self.tool_layout.addWidget(self.label)

        self.setting_btn = QPushButton(self)
        self.setting_btn.setObjectName('button')
        self.setting_btn.setText("")
        self.tool_layout.addWidget(self.setting_btn)

        self.save_btn = QPushButton(self)
        self.save_btn.setObjectName('button')
        self.save_btn.setText("保存")
        self.save_btn.resize(20, 20)
        self.save_btn.clicked.connect(self.save_file)
        self.tool_layout.addWidget(self.save_btn)

        self.extend_btn = QPushButton(self)
        self.extend_btn.setObjectName('button')
        self.extend_btn.setText("打开日历")
        self.extend_btn.clicked.connect(self.more)
        self.tool_layout.addWidget(self.extend_btn)


        self.label.setStyleSheet('''
                                    QLabel{
                                        color: white;    
                                    }
                                ''')

        self.save_btn.setStyleSheet('''
                                        QPushButton{
                                            border:none;
                                            color:white;
                                        }
                                        QPushButton#button{
                                            border:none;
                                            font-size:18px;
                                            font-weight:700;
                                            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                        }
                                        QPushButton#button:hover{
                                            font-weight:700;
                                            border-bottom: 3px solid white;
                                        }
                                    ''')

        self.setting_btn.setStyleSheet('''
                                                QPushButton{
                                                    border:none;
                                                    color:white;
                                                }
                                            ''')

        self.extend_btn.setStyleSheet('''
                                        QPushButton{
                                                border:none;
                                                color:white;
                                            }
                                            QPushButton#button{
                                                border:none;
                                                font-size:14px;
                                                font-weight:100;
                                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                            }
                                            QPushButton#button:hover{
                                                font-weight:700;
                                            }    
                                    ''')

        self.textbox = QTextEdit(self)
        self.textbox.resize(200, 300)
        task = self.open_file(self.time)
        if task:
            self.textbox.setText(task)
        else:
            self.textbox.setText("今天什么任务都没有哦~")
        self.textbox_layout.addWidget(self.textbox)

        self.main_layout.setSpacing(0)

        self.setGeometry(1200, 300, 300, 220)
        self.setWindowTitle('备忘录')
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setMinimumSize(350, 550)
        self.setMaximumSize(350, 550)
        self.setWindowIcon(QIcon('title.jfif'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.show()

    def get_time(self, date):
        self.time = date.toString("yyyy-MM-dd")
        self.label.setText(self.time)
        task = self.open_file(self.time)
        if task:
            self.textbox.setText(task)
        else:
            self.textbox.setText("今天什么任务都没有哦~")

    def open_file(self,title):
        if os.path.exists('./Note/'+title):
            with open('./Note/' + title, 'r', encoding="utf-8") as f:
                return f.read()
        else:
            return '今天什么任务都没有哦~'

    def save_file(self):
        new_task = self.textbox.toPlainText()
        with open('./Note/'+self.time, 'w', encoding='utf-8') as file_object:
            file_object.write(new_task)

    def more(self):
        self.hide()
        self.objectMemo = Memo()
        self.objectMemo.show()





