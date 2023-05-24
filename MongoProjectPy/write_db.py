import cdb
from datetime import datetime


def write(as_x, as_y, as_z, angle_x, angle_y, angle_z, temp):
    data = [{"Date": datetime.now().date()},
            {"Time": datetime.now().time()},
            {"acceleration X": as_x},
            {"acceleration Y": as_y},
            {"acceleration Z", as_z},
            {"angle X": angle_x},
            {"angle Y": angle_y},
            {"angle Z": angle_z},
            {"temperature": temp}]
    print("ПОЛУЧИЛИ В data: ", data)
    cdb.start_base().insert_one(data)
