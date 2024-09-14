import cx_Oracle

class Class:
    def __init__(self, id,name,teacher_id):
        if id is None:
            id = 0
        else:
            self.id = id
        self.name = name
        self.teacher_id = teacher_id

    @staticmethod
    def CreateClass(out_cursor):
        list = []
        try:
            for row in out_cursor.getvalue():
                list.append(Class(row[0],row[1],row[2]))
        except cx_Oracle.Error as error:
            print(error)
            return None
        return list