class CacheFile:
    def __init__(self, directory, filename, size, file):
        self.directory = directory
        self.size = size
        self.filename = filename
        self.__file = file

    def get_file(self):
        self.__file.seek(0, 0)
        return self.__file

    def close(self):
        self.__file.close()
