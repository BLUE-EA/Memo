# python3
# -*- coding: utf-8 -*-

import sys
from Memo import Memo
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    memo = Memo()
    sys.exit(app.exec_())