# summer
**A excel report helper**

**This is a toy. Its purpose is to savs as much time as possible.**

Installation
------------

summer is not support pip at present.

summer is conveniently available via`setup.py`
```
python setup.py install
```

To ensure summer is properly installed, you can run the import command in python environment:
```
import summer 
```

Usage
-----
The summer library enables you to quickly completes daily reports.

```python
import summer

if __name__ == "__main__":
    name = "sheetname" 
    filepath = r"C:"
    columns = ["Date", "Area"]
    file = summer.read_excel(name, filepath, columns)
    core_file = r"C:"
    fils = summer.files(core_file)
    files.register(file)
    files.process_file()
```

Cpoy Pastes!
-----
