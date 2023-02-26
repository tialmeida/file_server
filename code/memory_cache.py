import os
import file_in_cache


def get_key(directory, filename):
    return f'{directory}/{filename}'


class MemoryCache:
    def __init__(self, max_size):
        self.__files = {}
        self.__max_size = max_size
        self.__used_memory_cache = 0

    def get_file(self, directory, filename):
        file = self.__files.get(get_key(directory, filename))
        return file.get_file(), file.size

    def exist_file_in_cache(self, directory, filename):
        file = self.__files.get(get_key(directory, filename))

        if file is None:
            return False
        else:
            return True

    def add_file(self, directory, filename, file):
        file_size = os.path.getsize(get_key(directory, filename))

        if file_size > self.__max_size:
            return False
        elif file_size == self.__max_size:
            self.clear_memory()

        self.__add_file(directory, filename, file_size, file)
        self.__used_memory_cache += file_size
        return True

    def __add_file(self, directory, filename, file_size, file):
        if file_size + self.__used_memory_cache > self.__max_size:
            self.__free_up(file_size)

        self.__files[get_key(directory, filename)] = file_in_cache.CacheFile(directory, filename, file_size, file)

    def __free_up(self, bytes_to_free_up):
        free_space = 0

        for key in self.__files.keys():
            free_space += self.__files[key].size
            self.__files[key].close()
            self.__files.pop(key)

            if free_space >= bytes_to_free_up:
                break

    def clear_memory(self):
        for file in self.__files.values():
            file.close()

        self.__files.clear()
        self.__used_memory_cache = 0