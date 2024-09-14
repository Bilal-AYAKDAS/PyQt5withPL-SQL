import cx_Oracle

class Student:
    def __init__(self, id, student_number, name, surname,birthdate,gender,class_id):
        if id is None:
            id = 0
        else:
            self.id = id
        self.student_number = student_number         
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.class_id = class_id
    
    @staticmethod
    def CreateStudent(out_cursor):
        list = []
        try:
            for row in out_cursor.getvalue():
                list.append(Student(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        except cx_Oracle.Error as error:
            print(error)
            return None
        return list

    
        