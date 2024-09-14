import cx_Oracle
from datetime import datetime
from connection import conn
from Model.Student import Student
from Model.Teacher import Teacher
from Model.Class import Class
from Model.Lesson import Lesson
from Model.classlesson import ClassLesson

class DBManager:
    def __init__(self):
        self.connection = conn
        self.cursor = self.connection.cursor()

###Student Operations ###

    def getStudentById(self,id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_STUDENTS_BYID",out_cursor, [id])
        return Student.CreateStudent(out_cursor)

    def getStudentsByClassId(self,class_Id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_STUDENTS_BYCLASSID",out_cursor, [class_Id])
        return Student.CreateStudent(out_cursor)

    def getAllStudents(self,student_id,class_id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_ALL_STUDENTS",out_cursor,[student_id,class_id])
        return Student.CreateStudent(out_cursor)

    def addStudent(self,student:Student):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.STUDENT_PUT",out_number,[student.student_number,student.name,student.surname,student.birthdate,student.gender,student.class_id])
        out_number = out_number.getvalue()
        return out_number

    def editStudent(self,student:Student):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.STUDENT_UPDATE",out_number,[student.id,student.student_number,student.name,student.surname,student.birthdate,student.gender,student.class_id])
        out_number = out_number.getvalue()
        return out_number

    def deleteStudent(self,id):
        self.cursor.callproc("PYTHONORA.SCHOOL_PKG.STUDENT_DELETE",[id])


###Teacher Operations ###
    def getTeacherById(self,id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_TEACHER_BY_ID",out_cursor, [id])
        return Teacher.CreateTeacher(out_cursor)

    def getTeachersByBranch(self,branch):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_TEACHERS_BY_BRANCH",out_cursor, [branch])
        return Teacher.CreateTeacher(out_cursor)

    def getAllTeachers(self,id,branch):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_ALL_TEACHERS",out_cursor,[id,branch])
        return Teacher.CreateTeacher(out_cursor)

    def addTeacher(self,teacher:Teacher):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.TEACHER_PUT",out_number,[teacher.name,teacher.surname,teacher.birthdate,teacher.gender,teacher.branch])
        out_number = out_number.getvalue()
        return out_number

    def editTeacher(self,teacher:Teacher):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.TEACHER_UPDATE",out_number,[teacher.id,teacher.name,teacher.surname,teacher.birthdate,teacher.gender,teacher.branch])
        out_number = out_number.getvalue()
        return out_number

    def deleteTeacher(self,id):
        self.cursor.callproc("PYTHONORA.SCHOOL_PKG.TEACHER_DELETE",[id])
    
    ###Class Operations ###
    def getClassById(self,id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_CLASS_BY_ID",out_cursor, [id])
        return Class.CreateClass(out_cursor)

    def getClassByTeacherId(self,teacher_id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_CLASES_BY_TEACHERID",out_cursor, [teacher_id])
        return Class.CreateClass(out_cursor)

    def getAllClasses(self,id,teacher_id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_ALL_CLASSES",out_cursor,[id,teacher_id])
        return Class.CreateClass(out_cursor)

    def addClass(self,class_1:Class):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.CLASS_PUT",out_number,[class_1.name,class_1.teacher_id])
        out_number = out_number.getvalue()
        return out_number

    def editClass(self,class_1:Class):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.CLASS_UPDATE",out_number,[class_1.id,class_1.name,class_1.teacher_id])
        out_number = out_number.getvalue()
        return out_number

    def deleteClass(self,id):
        self.cursor.callproc("PYTHONORA.SCHOOL_PKG.CLASS_DELETE",[id])

 ## Lesson Operations ##
    def getLessonById(self,id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_LESSON_BY_ID",out_cursor, [id])
        return Lesson.CreateLesson(out_cursor)

    def getLessonsByLessonName(self,lesson_name):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_LESSONS_BY_NAME",out_cursor, [lesson_name])
        return Lesson.CreateLesson(out_cursor)

    def getAllLessons(self,id,lesson_name):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_ALL_LESSONS",out_cursor,[id,lesson_name])
        return Lesson.CreateLesson(out_cursor)

    def addLesson(self,lesson:Lesson):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.LESSON_PUT",out_number,[lesson.name])
        out_number = out_number.getvalue()
        return out_number

    def editLesson(self,lesson:Lesson):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.LESSON_UPDATE",out_number,[lesson.id,lesson.name])
        out_number = out_number.getvalue()
        return out_number

    def deleteLesson(self,id):
        self.cursor.callproc("PYTHONORA.SCHOOL_PKG.LESSON_DELETE",[id])


 ## ClassLesson Operations ##
    def getClassLessonById(self,id):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_CLASSLESSON_BY_ID",out_cursor, [id])
        return ClassLesson.CreateClassLesson(out_cursor)
    
    def getAllClassLessons(self,id,class_id,class_name,lesson_id,lesson_name,teacher_id,teacher_name):
        out_cursor = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.callfunc("PYTHONORA.SCHOOL_PKG.GET_ALL_CLASSLESSONS",out_cursor,[id,class_id,class_name,lesson_id,lesson_name,teacher_id,teacher_name])
        return ClassLesson.CreateClassLesson(out_cursor)
    
    def addClassLesson(self,classlesson:ClassLesson):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.CLASS_LESSON_PUT",out_number,[classlesson.class_id,classlesson.lesson_id,classlesson.teacher_id])
        out_number = out_number.getvalue()
        return out_number

    def editClassLesson(self,classlesson:ClassLesson):
        out_number = self.cursor.var(cx_Oracle.NUMBER)
        self.cursor.callfunc ("PYTHONORA.SCHOOL_PKG.CLASS_LESSON_UPDATE",out_number,[classlesson.id,classlesson.class_id,classlesson.lesson_id,classlesson.teacher_id])
        out_number = out_number.getvalue()
        return out_number
    
    def deleteClassLesson(self,id):
        self.cursor.callproc("PYTHONORA.SCHOOL_PKG.CLASS_LESSON_DELETE",[id])

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("Connection Closed")

db = DBManager()
# classLessons =db.getAllClassLessons(0,0,"",0,"",0,"")



