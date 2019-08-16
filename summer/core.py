# -*- coding:utf-8 -*-
"""
summer.core
~~~~~~~~~~~

This module provides a File to keep data from a file or query, provides a 
FileCollection to manage and process all file and provides a XlExceler to operates excel.
"""
import os
import logging

import pandas as pd
import xlwings as xl

from . import errors
from . import utils
from .excel import BaseExceler


class DataFrameWrapper:
    """Wrap DataFrame"""

    def __init__(self, dataframe: pd.DataFrame):
        """
        :params dataframe: A DataFrame.
        :return:
        """
        self._dataframe = dataframe
    
    def __call__(self):
        """
        DataFrameWrapper() -> pd.DataFrame
        :params:
        :return self._dataframe:
        """
        return self._dataframe


class File:
    """A file, from a read, from a database."""
    __slots__ = ["_method", "_name", "_filepath", "_columns", "_contents"]

    def __init__(self, method: str, name: str, filepath: str, columns: list):
        # read mthod
        self._method = method
        # sheetname
        self._name = name
        # the route of a file
        self._filepath = filepath
        # required fields
        self._columns = columns
        # file's contents
        self._contents = self._read()
    
    def __repr__(self):
        return "<File %s>" % self.method()
    
    def method(self) -> str:
        """File.method() -> str

        :param:
        :return self._method:
        """
        return self._method
    
    def name(self) -> str:
        """File.name() -> str

        :param:
        :return self._name:
        """
        return self._name
    
    def filepath(self) -> str:
        """File().filepath() -> str

        :params:
        :return self._filepath:
        """
        return self._filepath
    
    def columns(self) -> list:
        """File().columns() -> list

        :params:
        :return self._columns:
        """
        return self._columns
    
    def _scanning(self) -> list:
        """Scanning a file directory, and return a list of some file name.

        :params:
        :return list:
        :rtype: list
        """
        if not os.path.exists(self.filepath()):
            raise errors.FilePathError()
        file_names = os.listdir(self.filepath())
        return file_names
        
    
    def _read(self) -> pd.DataFrame:
        """Read file or query from database.

        :params:
        :return pd.DataFrame:
        :rtype: pd.DataFrame
        """
        file_names = self._scanning()
        full_file_path = utils.filename_match(name=self.name(), 
                                              file_path=self.filepath(), 
                                              file_names=file_names)
        if self.method() == "read_excel":
            return pd.read_excel(full_file_path)
        if self.method() == "read_csv":
            encoding = utils.chardet_file(full_file_path)
            return pd.read_csv(full_file_path, encoding=encoding)
    

    def contents(self) -> 'DataFrameWrapper':
        """Return a :class:`DataFrameWrapper` object.

        :params:
        :return DataFrameWrapper:
        :rtype: core.DataFrameWrapper
        """
        dataframewrapper = DataFrameWrapper(self._contents)
        return dataframewrapper()
    
    def clean(self, column_src: str, column_dst: str, clean_func: 'function'):
        """Add new filed and processing file's contens

        :param column_src: old field.
        :param column_dst: new filed.
        :param clean_func: data cleaning func.
        :return:
        """
        if not isinstance(self.columns(), list):
            raise errors.FileColumnsError()
        self._contents = self._contents[self.columns()]
        self._contents[column_dst] = self._contents[column_src].apply(clean_func)
        self._contents= self._contents.loc[self._contents[column_dst] != ""]

        


class FileCollection:
    """A set of Files from many register"""

    def __init__(self, core_file: str):
        self._core_file = core_file
        self._files = {}
        self._excel_init()
    
    def __repr__(self):
        return "<FileCollection size={} core_file={}>".format(len(self), self._core_file)

    def __len__(self):
        return len(self._files)

    def files(self):
        """Files.files() -> dict.
        
        :params:
        :return:
        """
        return self._files
    
    def register(self, file: 'File'):
        """Register File in Files.

        :param file: File to operates in the body of Files.
        :return:
        """
        if file.name() not in self._files:
            self._files[file.name()] = file
    
    def _excel_init(self):
        """Excel operation initialization.

        :params:
        :return:
        """
        self.excel = XlExceler()

    
    def process_file(self):
        """Process all file into excel file.

        :params:
        :return:
        """
        self.excel.open(self._core_file)
        #  逐个迭代出数据
        for key, value in self._files.items():
            self.excel.paste(key, value)
        #  保存、退出工作薄
        self.excel.close()


class XlExceler(BaseExceler):
    """Wrap xlwings, make sure excel operator easy to replaceable"""

    def open(self, file: "File"):
        """
        :params file:
        :return:
        """
        self.app = xl.App(add_book=False)
        self.app.visible = False
        self.app.display_alerts = False
        self.app.screen_updating = False
        self.wb = self.app.books.open(file)

    def paste(self, sheet_name: str, data: "File"):
        """
        :params file:
        :return:
        """
        sheet = self.wb.sheets[sheet_name]
        range_down_str = sheet.range("A1").end("down").get_address(False, False)[1:]
        range_down_num = int(range_down_str)
        if range_down_num != 1048576:
            range_down_num = range_down_num + 1
        else:
            range_down_num = 2
        sheet.range("J1").value = "1"
        sheet.range("A{}".format(range_down_num)).options(index=False, header=False).value = data.contents()

    def close(self):
        """Quit excel application.

        :params:
        :return:
        """
        self.wb.save()
        self.wb.close()
        self.app.display_alerts = True
        self.app.screen_updating = True
        self.app.quit()

if __name__ == "__main__":
    pass