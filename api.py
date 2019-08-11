# -*- coding: utf-8 -*-
"""
summer.api
~~~~~~~~~~

This module implements the Reads API and OPERATES API.

:author: Andy Yang.
"""

from core import File, FileCollection

def file(method:str, name: str, filepath: str, columns: list) -> "File":
    r"""Constructs a :class:`File <File>`.

    :param method: method for the new :class:`File` object.
    :param name: Location on xlsx when transferring data.
    :param filepath: filepath for the new :class:`File` object.
    :param columns: columns for the new :class:`File` object. 

    Usage:
      >>> import summer
      >>> f = summer.file("read_excel", "sheetname", "C:\example.xlsx", ["columnname"])
      <File read_excel>
    """

    return File(method=method, name=name, filepath=filepath, columns=columns)

def read_excel(name: str, filepath: str, columns: list) -> "File":
    r"""Reads a EXCEL file.
    
    :param name: Location on xlsx when transferring data.
    :param filepath: filepath for the new :class:`File` object.
    :param columns: columns for the new :class:`File` object.
    :return: :class:`File <File>` object.
    :rtype: core.File
    """

    return file("read_excel", name=name, filepath=filepath, columns=columns)

def read_csv(name: str, filepath: str, columns: list):
    r"""Reads a CSV file.
    
    :param name: Location on xlsx when transferring data.
    :param filepath: filepath for the new :class:`File` object.
    :param columns: columns for the new :class:`File` object.
    :return: :class:`File <File>` object.
    :rtype: core.File
    """

    return file("read_csv", name=name, filepath=filepath, columns=columns)

def files(core_file: str) -> "FileCollection":
    r"""Constructs a :class:`FileCollection <FileCollection>`.
    
    :param core_file: core_file for the new :class:`FileCollection` object.

    Usage:
      >>> import summer
      >>> fs = summer.files("C:\corefile.xlsx")
      <FileCollection size=0 core_file=C:\corefile.xlsx>
    """
    
    return FileCollection(core_file=core_file)

if __name__ == "__main__":
      pass