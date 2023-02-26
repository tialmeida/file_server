import sys
import tqdm
import socket
import utils


host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]
directory = ''
command_list_was_not_used = filename != utils.LIST_COMMAND and filename != utils.LIST_COMMAND.upper()

if command_list_was_not_used:
    directory = sys.argv[4]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.connect((host, port))
except ConnectionRefusedError:
    print(f'Host {host} and port {port} not found')
    exit()


def list_files():
    server.send(utils.LIST_COMMAND.encode(utils.ENCODE_TYPE))
    print(server.recv(utils.BUFFER_SIZE).decode(utils.ENCODE_TYPE))


def get_file():
    server.send(f'{filename}'.encode(utils.ENCODE_TYPE))
    message = server.recv(utils.BUFFER_SIZE).decode(utils.ENCODE_TYPE)

    if message == utils.FILE_NOT_FOUND:
        print(f'File {filename} does not exist in the server')
        server.close()
        return

    file_size = int(message)
    progress = tqdm.tqdm(range(file_size), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    file = open(f'{directory}/{filename}', 'wb')

    while True:
        bytes_read = server.recv(utils.BUFFER_SIZE)

        if not bytes_read:
            break

        file.write(bytes_read)
        progress.update(len(bytes_read))

    file.close()


if command_list_was_not_used:
    get_file()
else:
    list_files()

server.close()
