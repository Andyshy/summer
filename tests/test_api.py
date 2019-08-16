# -*- coding:utf-8 -*-
import unittest

from api import read_csv, read_excel, file, files


class TestApi(unittest.TestCase):
    def test_read_excel(self):
        name = "B" 
        filepath = r"C:"
        columns = ["日期", "站点"]
        file = read_excel(name, filepath, columns)
        self.assertTrue(file.name(), "B")
    
    def test_read_csv(self):
        name = "20190810" 
        filepath = r"C:"
        columns = ["日期", "姓名","ID"]
        file = read_csv(name, filepath, columns)
        self.assertTrue(file.name(), "20190810")
    
    def test_file(self):
        name = "20190810" 
        filepath = r"C:"
        columns = ["日期", "姓名","ID"]
        f = file("read_csv", name, filepath, columns)
        self.assertTrue(f.name(), "20190810")
    
    def test_files(self):
        name = "20190810" 
        filepath = r"C:"
        columns = ["日期", "姓名","ID"]
        f = file("read_csv", name, filepath, columns)
        core_file = r"C:corefile.xlsx"
        fs = files(core_file)
        fs.register(f)
        fs.process_file()
        self.assertTrue(len(fs), 1)

if __name__ == "__main__":
    unittest.main()
        