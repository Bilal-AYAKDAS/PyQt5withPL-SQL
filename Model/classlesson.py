import cx_Oracle

class ClassLesson:
    def __init__(self, id,class_id,class_name,lesson_id,lesson_name,teacher_id,teacher_name):
        if id is None:
            id = 0
        else:
            self.id = id
        self.class_id = class_id
        self.class_name = class_name
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
    
    @staticmethod
    def CreateClassLesson(out_cursor):
        list = []
        try:
            for row in out_cursor.getvalue():
                list.append(ClassLesson(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        except cx_Oracle.Error as error:
            print(error)
            return None
        return list