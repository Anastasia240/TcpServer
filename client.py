import secrets
import socket
import string

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:
    for _ in range(10000):
        bbbb = f'{secrets.randbelow(9999):04}'  # BBBB - номер участника
        nn = f"C{secrets.choice(string.digits)}"  # NN - id канала
        hh = f'{secrets.randbelow(6):02}'  # HH - Часы
        mm = f'{secrets.randbelow(60):02}'  # MM - минуты
        ss = f'{secrets.randbelow(60):02}'  # SS - секунды
        zhq = f'{secrets.randbelow(1000):03}'  # zhq - десятые сотые тысячные
        gg = f'{secrets.randbelow(20):02}'  # GG - номер группы
        message = f'{bbbb} {nn} {hh}:{mm}:{ss}.{zhq} {gg}\n'
        # if len(message.encode()) < 100:
        #     sock.sendall(f'{(len(message.encode())):02}'.encode())
        #     sock.sendall(message.encode())
        sock.sendall(message.encode())

finally:
    print('Закрываем сокет')
    sock.close()
