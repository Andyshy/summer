# -*- coding:utf-8 -*-
"""
summer.errors
~~~~~~~~~~~~~

This module provides some customize exception class.
"""


class FileColumnsError(Exception):
    def __init__(self):
        """File中传入的Columns必须是一个list"""


class FilePathError(Exception):
    def __init__(self):
        """文件路径不存在"""

if __name__ == "__main__":
    pass
