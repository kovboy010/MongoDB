import cdb
from datetime import datetime


# Модуль записи данных в БД.
def write_in(as_x, as_y, as_z, angle_x, angle_y, angle_z, temp):
    data = {
        "Date": str(datetime.now().strftime('%d/%m/%Y')),
        "Time": str(datetime.now().strftime('%H:%M:%S')),
        "acceleration X": as_x,
        "acceleration Y": as_y,
        "acceleration Z": as_z,
        "angle X": angle_x,
        "angle Y": angle_y,
        "angle Z": angle_z,
        "temperature": temp
    }
    print("ПОЛУЧИЛИ В data: ", data)
    cdb.start_base().insert_one(data)

# a_x = 10
# a_y = 20.12
# a_z = 30.76
# angl_x = 90.80
# angl_y = 10.71
# angl_z = 120.11
# tem = 80.18
#
# a_x = a_x + 7
# a_y = a_y + 7
# a_z = a_z + 7
# angl_x = angl_x + 7
# angl_y = angl_y + 7
# angl_z = angl_z + 7
# tem = tem + 7
#
# write_in(a_x, a_y, a_z, angl_x, angl_y, angl_z, tem)
