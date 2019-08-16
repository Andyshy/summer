# -*- coding:utf-8 -*-
"""
summer.excel
~~~~~~~~~~~~

This module provides a excel base class to standardize excel operation.
"""
from abc import ABCMeta,abstractmethod

class BaseExceler(metaclass = ABCMeta):
    @abstractmethod
    def open(self, file: str):
        """
        Open a excel application with file's path.
        :params file:
        :return:
        """
    
    @abstractmethod
    def paste(self, sheet_name: str, data: "File"):
        """
        Transfer data to excel.
        :params:
        :return:
        """
    
    @abstractmethod
    def close(self):
        """
        Save,close excel application.
        :params:
        :return:
        """