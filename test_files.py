# -*- coding:utf-8 -*-
import unittest

import pandas as pd

import core
import api

def choose_shenzhen(x):
    if "深圳" in x:
        return x
    return ""


class TestFile(unittest.TestCase):
    def test_file_attr(self):
        method = "read_excel"
        name = "B" 
        filepath = r"C:"
        columns = ["日期", "站点"]
        file = core.File(method, name, filepath, columns)
        self.assertEqual(file.name(), "B")
        self.assertEqual(file.method(), "read_excel")
        self.assertEqual(file.filepath(), r"C:")
        self.assertEqual(file.columns(), ["日期", "站点"])
    
    def test_file_contents(self):
        method = "read_excel"
        name = "B" 
        filepath = r"C:"
        columns = ["日期", "站点"]
        file = core.File(method, name, filepath, columns)
        self.assertEqual(file.contents().shape, (317, 48))
    
    def test_file_clean(self):
        method = "read_excel"
        name = "B" 
        filepath = r"C:"
        columns = ["日期", "站点"]
        file = core.File(method, name, filepath, columns)
        file.clean(column_src="站点", column_dst="深圳", clean_func=choose_shenzhen)
        self.assertEqual(file.contents().shape, (85, 6))


class TestFileCollection(unittest.TestCase):
    def test_filecollection_registr(self):
        method = "read_excel"
        name = "B" 
        filepath = r"C:"
        columns = ["日期", "站点"]
        file = core.File(method, name, filepath, columns)
        core_file = r"C:corefile.xlsx"
        filecollection = core.FileCollection(core_file)
        filecollection.register(file)
        self.assertTrue(filecollection.files().get("B"))
    
    def test_filecollection_process_file(self):
        method = "read_excel"
        name = "B" 
        filepath = r"C:"
        columns = ["日期", "站点"]
        file = core.File(method, name, filepath, columns)
        core_file = r"C:"
        filecollection = core.FileCollection(core_file)
        filecollection.register(file)
        filecollection.process_file()


if __name__ == "__main__":
    unittest.main()