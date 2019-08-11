# -*- coding:utf-8 -*-
"""
summer.utils
~~~~~~~~~~~~

This module provides some utility methods.
"""
import chardet
import os

def filename_match(name: str, file_path: str, file_names: list) -> str:
    """Return a full file path.

    :params name, file_path, file_names:
    :return:
    """
    for file_name in file_names:
        if name not in file_name:
            continue
        full_file_path = os.path.join(file_path, file_name)
        break
    return full_file_path

def chardet_file(full_file_path: str) -> str:
    """Return a file's encoding.

    :param full_file_path:
    :return:
    """
    with open(full_file_path, "rb") as f:
        data = f.read(256)
        return chardet.detect(data).get("encoding")