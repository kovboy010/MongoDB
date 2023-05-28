import serial
import write_db
import numpy as np


# Подключение к serial порту.
def ser_connect():
    sr = serial.Serial('COM7', 9600)
    return sr


# Предобработка данных.
def presort():
    while True:
        check_byte = ser_connect().read(1)
        if check_byte == 0x7E:
            leng = ser_connect().read(2)
            leng_int = int.from_bytes(leng, 'big')
            mass = np.zeros(1, leng_int)
            mass[0] = 0x7E
            mass[1] = leng[0]
            mass[2] = leng[1]
            for i in range(leng_int - 3):
                mass[i + 3] = ser_connect().read(1)
            crc_now = 0
            for i in range(leng_int + 2):
                crc_now += mass[i + 3]
            crc_now = 0xFF - crc_now
            if (crc_now == mass[leng_int]):
                re = []
                for i in range(leng_int + 16):
                    re.append(mass[i + 17])
                return re


# Распределение и запись данных в БД.
def separation_put():
    mass = presort()
    acceleration_x = mass[0:7]
    acceleration_y = mass[8:15]
    acceleration_z = mass[16:23]
    angle_x = mass[24:31]
    angle_y = mass[32:39]
    angle_z = mass[40:47]
    temperature = mass[48:55]
    # write_db.write_in(acceleration_x, acceleration_y, acceleration_z, angle_x, angle_y, angle_z, temperature)
