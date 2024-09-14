import cx_Oracle

class Teacher:
    def __init__(self, id, branch, name, surname,birthdate,gender):
        if id is None:
            id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def CreateTeacher(out_cursor):
        list = []
        try:
            for row in out_cursor.getvalue():
                list.append(Teacher(row[0],row[1],row[2],row[3],row[4],row[5]))
        except cx_Oracle.Error as error:
            print(error)
            return None
        return list