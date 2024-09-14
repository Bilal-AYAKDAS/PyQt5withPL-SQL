import cx_Oracle

class Lesson:
    def __init__(self, id,name):
        if id is None:
            id = 0
        else:
            self.id = id
        self.name = name
    
    @staticmethod
    def CreateLesson(out_cursor):
        list = []
        try:
            for row in out_cursor.getvalue():
                list.append(Lesson(row[0],row[1]))
        except cx_Oracle.Error as error:
            print(error)
            return None
        return list