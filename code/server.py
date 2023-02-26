import os
import socket
import sys
from _thread import *
import tqdm
import memory_cache
import utils


port = int(sys.argv[1])
directory = sys.argv[2]


def client_main(client_connection, client_address):
    filename = client_connection.recv(utils.BUFFER_SIZE).decode(utils.ENCODE_TYPE)

    if filename == utils.LIST_COMMAND:
        print(f'{client_address[0]} listing files')
        list_files(client_connection)
    else:
        print(f'{client_address[0]} is requesting file {filename}')
        send_file(client_connection, filename)

    client_connection.close()


def list_files(client_connection):
    files = ''

    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        files = 'Error. Directory not found'

    client_connection.send(f'{transform_file_list(files)}'.encode(utils.ENCODE_TYPE))


def transform_file_list(files):
    files_string_list = ''

    for file in files:
        files_string_list += f'{file}\n'

    return files_string_list


def send_file(client_connection, filename):
    file_size = None
    file = None

    if cache.exist_file_in_cache(directory, filename):
        file, file_size = cache.get_file(directory, filename)
        print(f' Cache hit. File {filename} sent to the client.')
    else:
        try:
            file = open(f'{directory}/{filename}', 'rb')
            file_size = os.path.getsize(f'{directory}/{filename}')
        except FileNotFoundError:
            print(f'File {filename} does not exist')
            client_connection.send(utils.FILE_NOT_FOUND.encode(utils.ENCODE_TYPE))
            return

        if cache.add_file(directory, filename, file):
            print(f' Cache miss. File {filename} sent to the client')
        else:
            print(f' Cache miss and file exceed the cache memory size. File {filename} sent to the client')

    client_connection.send(f'{file_size}'.encode(utils.ENCODE_TYPE))
    progress = tqdm.tqdm(range(file_size), f'{filename}', unit='B', unit_scale=True, unit_divisor=1024)

    while True:
        bytes_read = file.read(utils.BUFFER_SIZE)

        if not bytes_read:
            break

        client_connection.sendall(bytes_read)
        progress.update(len(bytes_read))


cache = memory_cache.MemoryCache(64 * 1000000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((utils.IP_ADDRESS, port))
server.listen(utils.CONNECTIONS_LIMIT)

while True:
    connection, address = server.accept()
    start_new_thread(client_main, (connection, address))
