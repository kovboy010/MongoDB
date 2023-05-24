import cdb

def sort(inp):
    f = cdb.start_base().find({"massage:"}, str(inp))
    print ("Получили из базы данных: ", f)