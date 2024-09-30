from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter

# Test the default class 
df = FileReaderWriter()
df.read()
df.write()

# Test the polymorphed methods
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write (filepath = "sample2.csv", data = ["Hello", "World"])

j = JSONFileReaderWriter()
j.read ("sample.json")
j.write (data = ['foo', {'bar': ('baz', None, 1.0, 2)}], filepath = "sample2.json")

t = TextFileReaderWriter()
t.read ("TextFileReaderWriter.txt")
t.write (filepath = "TextFileReaderWriter2.txt", data = ("TexttFileReaderWriter2 - new content"))