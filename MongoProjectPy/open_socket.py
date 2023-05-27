import socket
import threading
import command_module


def is_disconnect(command):
    command_module.disconnect()


# Функция отправки сообщений. Необходима для других модулей.
def send(data_db):
    print("я здесь 4")
    data_db.send(command_module.read(data_db).encode('utf-8'))
    print("я здесь 5")


# Прием сообщений
def recieve_handler(mess):
    while True:
        try:
            data = mess.recv(1024).decode('utf-8')
            print(data)
            if data == 'dis':
                print("Совединение завершено!")
                break
            print(data)
            mess.send(data.encode('utf-8'))
            command_module.handle_command(data)

            # command = command_module.handle_data(data)
            # if is_disconnect(command):
            #     break
            # command_module.execute(command)
        except Exception as e:
            print(f'ERROR Connection: {e}')
            break


# Открытие сокета для приема сообщений.
def op_sock_in():
    try:
        sock = socket.socket()
        sock.bind(('', 1112))
        sock.listen(3)
        print("socket created.")
        while True:
            conn, addr = sock.accept()
            threading.Thread(target=recieve_handler, args=(conn,)).start()
            print("connected client: ", addr)
            # return conn
    except Exception as e:
        print(f'An error has occurred when instancing socket: {e}')
        conn.close()
