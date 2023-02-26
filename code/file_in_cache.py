import utils


class CacheFile:
    def __init__(self, directory, filename, size, file):
        self.directory = directory
        self.size = size
        self.filename = filename
        self.__file = []

        while True:
            bytes_read = file.read(utils.BUFFER_SIZE)

            if not bytes_read:
                break

            self.__file.append(bytes_read)

        file.close()

    def get_file(self):
        return self.__file
