# class read
#class write (override)
from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read (self, filepath):
        with open (filepath, "r") as read_file:
            read_file.read()

    def write (self, filepath, data):
        with open(filepath, "w") as write_file:
            write_file.write(data)
