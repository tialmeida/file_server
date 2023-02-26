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

        if file is None:
            return None, None

        return file.get_file(), file.size

    def exist_file_in_cache(self, directory, filename):
        file = self.__files.get(get_key(directory, filename))

        if file is None:
            return False
        else:
            return True

    def add_file(self, directory, filename):
        try:
            file_size = os.path.getsize(get_key(directory, filename))
            file = open(f'{directory}/{filename}', 'rb')
        except FileNotFoundError:
            return None

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
        keys_to_remove = []

        for key in self.__files.keys():
            free_space += self.__files[key].size
            keys_to_remove.append(key)

            if free_space >= bytes_to_free_up:
                break

        for key in keys_to_remove:
            self.__files.pop(key)

        self.__used_memory_cache -= free_space

    def clear_memory(self):
        self.__files.clear()
        self.__used_memory_cache = 0
