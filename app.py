from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QComboBox, QDateEdit
from datetime import datetime
from dbmanager import DBManager
import sys
from View.UISchoolMenu import Ui_MainWindow as WindowMenu
from View.UIClassList import Ui_Classes as WindowClass
from View.UIStudentList import Ui_MainWindow as WindowStudent
from View.UITeacherList import Ui_MainWindow as WindowTeacher
from View.UILessonList import Ui_MainWindow as WindowLesson
from View.UIClassLessonList import Ui_MainWindow as WindowClassLesson
from Model.Student import Student
from Model.Teacher import Teacher
from Model.Class import Class
from Model.Lesson import Lesson
from Model.classlesson import ClassLesson


class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuWindow,self).__init__()
        self.ui = WindowMenu()
        self.ui.setupUi(self)
        
        self._classWindow = None
        self._studentWindow = None
        self._teacherWindow = None
        self._lessonWindow = None
        self._classlessonWindow = None
        self.ui.listWidget.itemClicked.connect(self.open_window)

        
    def open_window(self,item):
        if item.text() == "Öğrenci Listesi":
            self.open_student()
        elif item.text() == "Öğretmen Listesi":
            self.open_teacher()
        elif item.text() == "Sınıf Listesi":
            self.open_class()
        elif item.text() == "Ders Listesi":
            self.open_lesson()
        elif item.text() == "Sınıf - Ders Listesi":
            self.open_classlesson()

    def open_class(self):
        self._classWindow = ClassWindow()
        self._classWindow.show()

    def open_student(self):
        self._studentWindow = StudentWindow()
        self._studentWindow.show()

    def open_teacher(self):
        self._teacherWindow = TeacherWindow()
        self._teacherWindow.show()
    
    def open_lesson(self):
        self._lessonWindow = LessonWindow()
        self._lessonWindow.show()
    
    def open_classlesson(self):
        self._classlessonWindow = ClassLessonWindow()
        self._classlessonWindow.show()

class ClassWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ClassWindow, self).__init__(parent)
        self.db = DBManager()
        self.ui = WindowClass()
        self.ui.setupUi(self)
        self.load_classes()
        self.ui.btn_view.clicked.connect(self.load_classes)
        self.ui.btn_save.clicked.connect(self.save_class)
        self.ui.btn_new.clicked.connect(self.new_class)
        self.ui.btn_delete.clicked.connect(self.delete_class)
        self.ui.tbl_classes.cellDoubleClicked.connect(self.select_class)

    def load_classes(self):
        class_id = self.ui.txt_classid.text()
        teacher_id = self.ui.txt_teacher.text()
        classes = self.db.getAllClasses(class_id,teacher_id)

        self.ui.tbl_classes.setRowCount(len(classes))
        self.ui.tbl_classes.setColumnCount(3)
        self.ui.tbl_classes.setHorizontalHeaderLabels(["Class Id","Class Name","Teacher Id"])
        self.ui.tbl_classes.setColumnWidth(0,100)
        self.ui.tbl_classes.setColumnWidth(1,250)
        self.ui.tbl_classes.setColumnWidth(2,100)

        rowIndex = 0
        for _class in classes:
            self.ui.tbl_classes.setItem(rowIndex,0,QTableWidgetItem(str(_class.id)))
            self.ui.tbl_classes.setItem(rowIndex,1,QTableWidgetItem(str(_class.name)))
            self.ui.tbl_classes.setItem(rowIndex,2,QTableWidgetItem(str(_class.teacher_id)))
            rowIndex += 1

    def new_class(self):
        self.ui.tbl_classes.insertRow(0)
        item = QTableWidgetItem("-1")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Hücreyi salt okunur yap
        self.ui.tbl_classes.setItem(0, 0, item)

    def save_class(self):
        row_count = self.ui.tbl_classes.rowCount()
        for row in range(row_count):
            item_id = int(self.ui.tbl_classes.item(row, 0).text())
            item_classname = self.ui.tbl_classes.item(row, 1).text()
            item_teacherid = self.ui.tbl_classes.item(row, 2).text()
            if item_id == -1:
                print("Insert")
                _class = Class(-1, item_classname, item_teacherid)
                self.db.addClass(_class)
            else:
                _class = Class(item_id, item_classname, item_teacherid)
                self.db.editClass(_class)
        self.load_classes()
        print("Save")

    def select_class(self,row,column):
        # Seçili satırdaki verileri alın
        class_id = self.ui.tbl_classes.item(row, 0).text()
        class_name = self.ui.tbl_classes.item(row, 1).text()
        
        # Verileri ana pencereye aktarın
        if self.parent() is not None:
            self.parent().set_class_data(class_id, class_name)

    def delete_class(self):
        selected_row_index = self.ui.tbl_classes.currentRow()
        print(selected_row_index)
        if selected_row_index >= 0:
            selected_id = self.ui.tbl_classes.item(selected_row_index, 0)
            self.db.deleteClass(selected_id.text())
            self.load_classes()           
        else:
            QMessageBox.information(self, "Uyarı", "Lütfen ilk Önce Bir Satır Seçiniz ?", QMessageBox.Ok )
           
class StudentWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentWindow,self).__init__()
        self.db = DBManager()
        self.ui = WindowStudent()
        self.ui.setupUi(self)
        self.load_students()
        self.ui.btn_view.clicked.connect(self.load_students)
        self.ui.btn_save.clicked.connect(self.save_students)
        self.ui.btn_new.clicked.connect(self.new_student)
        self.ui.btn_delete.clicked.connect(self.delete_student)

    def load_students(self):
        student_id = self.ui.txt_studentid.text()
        class_id = self.ui.txt_classid.text()
        students = self.db.getAllStudents(student_id,class_id)

        self.ui.tbl_students.setRowCount(len(students))
        self.ui.tbl_students.setColumnCount(7)

        self.ui.tbl_students.setHorizontalHeaderLabels(["Id","Number","Name","Surname","Birthdate","Gender","Class Id"])
        self.ui.tbl_students.setColumnWidth(0,50)
        self.ui.tbl_students.setColumnWidth(1,150)
        self.ui.tbl_students.setColumnWidth(2,150)
        self.ui.tbl_students.setColumnWidth(3,150)
        self.ui.tbl_students.setColumnWidth(4,100)
        self.ui.tbl_students.setColumnWidth(5,100)
        self.ui.tbl_students.setColumnWidth(6,100)

        rowIndex = 0
        for student in students:
            self.ui.tbl_students.setItem(rowIndex,0,QTableWidgetItem(str(student.id)))
            self.ui.tbl_students.setItem(rowIndex,1,QTableWidgetItem(str(student.student_number)))
            self.ui.tbl_students.setItem(rowIndex,2,QTableWidgetItem(str(student.name)))
            self.ui.tbl_students.setItem(rowIndex,3,QTableWidgetItem(str(student.surname)))
            self.ui.tbl_students.setItem(rowIndex,4,QTableWidgetItem(student.birthdate.strftime("%d/%m/%Y")))
            self.ui.tbl_students.setItem(rowIndex,5,QTableWidgetItem(str(student.gender)))
            self.ui.tbl_students.setItem(rowIndex,6,QTableWidgetItem(str(student.class_id)))
            rowIndex += 1

    def new_student(self):
        self.ui.tbl_students.insertRow(0)
        item = QTableWidgetItem("-1")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Hücreyi salt okunur yap
        self.ui.tbl_students.setItem(0, 0, item)

        # 4. hücreye tarih seçici ekle
        item_date = QTableWidgetItem("MM/DD/YYYY")
        self.ui.tbl_students.setItem(0, 4, item_date)

    def save_students(self):
        row_count = self.ui.tbl_students.rowCount()
        for row in range(row_count):
            item_id = int(self.ui.tbl_students.item(row, 0).text())
            item_studentnum = self.ui.tbl_students.item(row, 1).text()
            item_name = self.ui.tbl_students.item(row, 2).text()
            item_surname = self.ui.tbl_students.item(row, 3).text()
            print(self.ui.tbl_students.item(row, 4).text())
            item_birthdate = datetime.strptime(self.ui.tbl_students.item(row, 4).text(), "%d/%m/%Y").date()
            item_gender = self.ui.tbl_students.item(row, 5).text()
            item_classid = int(self.ui.tbl_students.item(row, 6).text())
            student = Student(item_id, item_studentnum, item_name, item_surname, item_birthdate, item_gender, item_classid)
            if student.id == -1:
                print("Insert")
                self.db.addStudent(student)
            else:
                self.db.editStudent(student)
        self.load_students()
        print("Save")

    def delete_student(self):
        selected_row_index = self.ui.tbl_students.currentRow()
        print(selected_row_index)
        if selected_row_index >= 0:
            selected_id = self.ui.tbl_students.item(selected_row_index, 0)
            self.db.deleteStudent(selected_id.text())
            self.load_students()           
        else:
            QMessageBox.information(self, "Uyarı", "Lütfen ilk Önce Bir Satır Seçiniz ?", QMessageBox.Ok )
    
class TeacherWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(TeacherWindow,self).__init__(parent)
        self.db = DBManager()
        self.ui = WindowTeacher()
        self.ui.setupUi(self)
        self.load_teachers()
        self.ui.btn_view.clicked.connect(self.load_teachers)
        self.ui.btn_save.clicked.connect(self.save_teachers)
        self.ui.btn_new.clicked.connect(self.new_teacher)
        self.ui.btn_delete.clicked.connect(self.delete_teacher)
        self.ui.tbl_teachers.cellDoubleClicked.connect(self.select_teacher)


    def load_teachers(self):
        teacher_id = self.ui.txt_teacherid.text()
        branch = self.ui.txt_branch.text()
        teachers = self.db.getAllTeachers(teacher_id,branch)

        self.ui.tbl_teachers.setRowCount(len(teachers))
        self.ui.tbl_teachers.setColumnCount(6)

        self.ui.tbl_teachers.setHorizontalHeaderLabels(["Id","Branch","Name","Surname","Birthdate","Gender"])
        self.ui.tbl_teachers.setColumnWidth(0,50)
        self.ui.tbl_teachers.setColumnWidth(1,150)
        self.ui.tbl_teachers.setColumnWidth(2,150)
        self.ui.tbl_teachers.setColumnWidth(3,150)
        self.ui.tbl_teachers.setColumnWidth(4,100)
        self.ui.tbl_teachers.setColumnWidth(5,100)

        rowIndex = 0
        for teacher in teachers:
            self.ui.tbl_teachers.setItem(rowIndex,0,QTableWidgetItem(str(teacher.id)))
            self.ui.tbl_teachers.setItem(rowIndex,1,QTableWidgetItem(str(teacher.branch)))
            self.ui.tbl_teachers.setItem(rowIndex,2,QTableWidgetItem(str(teacher.name)))
            self.ui.tbl_teachers.setItem(rowIndex,3,QTableWidgetItem(str(teacher.surname)))
            self.ui.tbl_teachers.setItem(rowIndex,4,QTableWidgetItem(teacher.birthdate.strftime("%d/%m/%Y")))
            self.ui.tbl_teachers.setItem(rowIndex,5,QTableWidgetItem(str(teacher.gender)))
            rowIndex += 1

    def new_teacher(self):
        self.ui.tbl_teachers.insertRow(0)
        item = QTableWidgetItem("-1")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Hücreyi salt okunur yap
        self.ui.tbl_teachers.setItem(0, 0, item)

        # 4. hücreye tarih seçici ekle
        item_date = QTableWidgetItem("MM/DD/YYYY")
        self.ui.tbl_teachers.setItem(0, 4, item_date)

    def save_teachers(self):
        row_count = self.ui.tbl_teachers.rowCount()
        for row in range(row_count):
            item_id = int(self.ui.tbl_teachers.item(row, 0).text())
            item_branch =  self.ui.tbl_teachers.item(row, 1).text() 
            item_name =  self.ui.tbl_teachers.item(row, 2).text()
            item_surname = self.ui.tbl_teachers.item(row, 3).text()
            item_birthdate = datetime.strptime(self.ui.tbl_teachers.item(row, 4).text(), "%d/%m/%Y").date() 
            item_gender = self.ui.tbl_teachers.item(row, 5).text()
            teacher = Teacher(item_id, item_branch, item_name, item_surname, item_birthdate, item_gender)
            if teacher.id == -1:
                print("Insert")
                self.db.addTeacher(teacher)
            else:
                self.db.editTeacher(teacher)
        self.load_teachers()
        print("Save")
    
    def select_teacher(self,row,column):
        # Seçili satırdaki verileri alın
        teacher_id = self.ui.tbl_teachers.item(row, 0).text()
        teacher_name = self.ui.tbl_teachers.item(row, 2).text()
        
        # Verileri ana pencereye aktarın
        if self.parent() is not None:
            self.parent().set_teacher_data(teacher_id, teacher_name)

    def delete_teacher(self):
        selected_row_index = self.ui.tbl_teachers.currentRow()
        print(selected_row_index)
        if selected_row_index >= 0:
            selected_id = self.ui.tbl_teachers.item(selected_row_index, 0)
            self.db.deleteTeacher(selected_id.text())
            self.load_teachers()           
        else:
            QMessageBox.information(self, "Uyarı", "Lütfen ilk Önce Bir Satır Seçiniz ?", QMessageBox.Ok )

class LessonWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(LessonWindow,self).__init__(parent)
        self.db = DBManager()
        self.ui = WindowLesson()
        self.ui.setupUi(self)
        self.load_lessons()
        self.ui.btn_view.clicked.connect(self.load_lessons)
        self.ui.btn_save.clicked.connect(self.save_lesson)
        self.ui.btn_new.clicked.connect(self.new_lesson)
        self.ui.btn_delete.clicked.connect(self.delete_lesson)
        self.ui.tbl_lessons.cellDoubleClicked.connect(self.select_teacher)

    def load_lessons(self):
        lesson_id = self.ui.txt_lessonid.text()
        lesson_name = self.ui.txt_lessonname.text()
        lessons = self.db.getAllLessons(lesson_id,lesson_name)

        self.ui.tbl_lessons.setRowCount(len(lessons))
        self.ui.tbl_lessons.setColumnCount(2)
        self.ui.tbl_lessons.setHorizontalHeaderLabels([" Id","Lesson Name"])
        self.ui.tbl_lessons.setColumnWidth(0,50)
        self.ui.tbl_lessons.setColumnWidth(1,250)

        rowIndex = 0
        for _lesson in lessons:
            self.ui.tbl_lessons.setItem(rowIndex,0,QTableWidgetItem(str(_lesson.id)))
            self.ui.tbl_lessons.setItem(rowIndex,1,QTableWidgetItem(str(_lesson.name)))
            rowIndex += 1
    
    def select_teacher(self,row,column):
        # Seçili satırdaki verileri alın
        lesson_id = self.ui.tbl_lessons.item(row, 0).text()
        lesson_name = self.ui.tbl_lessons.item(row, 1).text()
        
        # Verileri ana pencereye aktarın
        if self.parent() is not None:
            self.parent().set_lesson_data(lesson_id, lesson_name)

    def new_lesson(self):
        self.ui.tbl_lessons.insertRow(0)
        item = QTableWidgetItem("-1")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Hücreyi salt okunur yap
        self.ui.tbl_lessons.setItem(0, 0, item)

    def save_lesson(self):
        row_count = self.ui.tbl_lessons.rowCount()
        for row in range(row_count):
            item_id = int(self.ui.tbl_lessons.item(row, 0).text())
            item_lessonname = self.ui.tbl_lessons.item(row, 1).text()
            if item_id == -1:
                print("Insert")
                _lesson = Lesson(-1, item_lessonname)
                self.db.addLesson(_lesson)
            else:
                _lesson = Lesson(item_id, item_lessonname)
                self.db.editLesson(_lesson)
        self.load_lessons()
        print("Save")

    def delete_lesson(self):
        selected_row_index = self.ui.tbl_lessons.currentRow()
        print(selected_row_index)
        if selected_row_index >= 0:
            selected_id = self.ui.tbl_lessons.item(selected_row_index, 0)
            self.db.deleteLesson(selected_id.text())
            self.load_lessons()           
        else:
            QMessageBox.information(self, "Uyarı", "Lütfen ilk Önce Bir Satır Seçiniz ?", QMessageBox.Ok )

class ClassLessonWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ClassLessonWindow,self).__init__()
        self.db = DBManager()
        self.ui = WindowClassLesson()
        self.ui.setupUi(self)
        self.load_classlessons()
        self.ui.btn_view.clicked.connect(self.load_classlessons)
        self.ui.btn_save.clicked.connect(self.save_classlesson)
        self.ui.btn_new.clicked.connect(self.new_classlesson)
        self.ui.btn_delete.clicked.connect(self.delete_classlesson)
        self.ui.btn_classselect.clicked.connect(self.select_class)
        self.ui.btn_lessonselect.clicked.connect(self.select_lesson)
        self.ui.btn_teacherselect.clicked.connect(self.select_teacher)
        self.class_window = None
        self.lesson_window = None
        self.teacher_window = None


    def load_classlessons(self):
        classlesson_id = self.ui.txt_classlessonid.text()
        class_id = self.ui.txt_classid.text()
        class_name = self.ui.txt_classname.text()
        lesson_id = self.ui.txt_lessonid.text()
        lesson_name = self.ui.txt_lessonname.text()
        teacher_id = self.ui.txt_teacherid.text()
        teacher_name = self.ui.txt_teachername.text()
        classlessons = self.db.getAllClassLessons(classlesson_id,class_id,class_name,lesson_id,lesson_name,teacher_id,teacher_name)
        self.ui.tbl_classlesson.setRowCount(len(classlessons))
        self.ui.tbl_classlesson.setColumnCount(7)
        self.ui.tbl_classlesson.setHorizontalHeaderLabels(["Id","Class Id","Class Name","Lesson Id","Lesson Name","Teacher Id","Teacher Name"])
        self.ui.tbl_classlesson.setColumnWidth(0,50)
        self.ui.tbl_classlesson.setColumnWidth(1,100)
        self.ui.tbl_classlesson.setColumnWidth(2,100)
        self.ui.tbl_classlesson.setColumnWidth(3,100)
        self.ui.tbl_classlesson.setColumnWidth(4,100)
        self.ui.tbl_classlesson.setColumnWidth(5,100)
        self.ui.tbl_classlesson.setColumnWidth(6,100)


        rowIndex = 0
        for classlesson in classlessons:
            self.ui.tbl_classlesson.setItem(rowIndex,0,QTableWidgetItem(str(classlesson.id)))
            self.ui.tbl_classlesson.setItem(rowIndex,1,QTableWidgetItem(str(classlesson.class_id)))
            self.ui.tbl_classlesson.setItem(rowIndex,2,QTableWidgetItem(str(classlesson.class_name)))
            self.ui.tbl_classlesson.setItem(rowIndex,3,QTableWidgetItem(str(classlesson.lesson_id)))
            self.ui.tbl_classlesson.setItem(rowIndex,4,QTableWidgetItem(str(classlesson.lesson_name)))
            self.ui.tbl_classlesson.setItem(rowIndex,5,QTableWidgetItem(str(classlesson.teacher_id)))
            self.ui.tbl_classlesson.setItem(rowIndex,6,QTableWidgetItem(str(classlesson.teacher_name)))
            rowIndex += 1

    def select_class(self):
        self.class_window = ClassWindow(self)
        self.class_window.show()
    
    def select_lesson(self):
        self.lesson_window = LessonWindow(self)
        self.lesson_window.show()

    def select_teacher(self):
        self.teacher_window = TeacherWindow(self)
        self.teacher_window.show()

    def set_class_data(self,class_id,class_name):
        row = self.ui.tbl_classlesson.currentRow()
        self.ui.tbl_classlesson.setItem(row, 1, QTableWidgetItem(class_id))
        self.ui.tbl_classlesson.setItem(row, 2, QTableWidgetItem(class_name))
        self.class_window.close()
    
    def set_lesson_data(self,lesson_id,lesson_name):
        row = self.ui.tbl_classlesson.currentRow()
        self.ui.tbl_classlesson.setItem(row, 3, QTableWidgetItem(lesson_id))
        self.ui.tbl_classlesson.setItem(row, 4, QTableWidgetItem(lesson_name))
        self.lesson_window.close()
    
    def set_teacher_data(self,teacher_id,teacher_name):
        row = self.ui.tbl_classlesson.currentRow()
        self.ui.tbl_classlesson.setItem(row, 5, QTableWidgetItem(teacher_id))
        self.ui.tbl_classlesson.setItem(row, 6, QTableWidgetItem(teacher_name))
        self.teacher_window.close()
    
    def new_classlesson(self):
        self.ui.tbl_classlesson.insertRow(0)
        item = QTableWidgetItem("-1")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Hücreyi salt okunur yap
        self.ui.tbl_classlesson.setItem(0, 0, item)

    def save_classlesson(self):
        row_count = self.ui.tbl_classlesson.rowCount()
        for row in range(row_count):
            item_id = int(self.ui.tbl_classlesson.item(row, 0).text())
            item_classid = self.ui.tbl_classlesson.item(row, 1).text()
            item_classname = self.ui.tbl_classlesson.item(row, 2).text()
            item_lessonid = self.ui.tbl_classlesson.item(row, 3).text()
            item_lessonname = self.ui.tbl_classlesson.item(row, 4).text()
            item_teacherid = self.ui.tbl_classlesson.item(row, 5).text()
            item_teachername = self.ui.tbl_classlesson.item(row, 6).text()
            if item_id == -1:
                print("Insert")
                _classlesson = ClassLesson(-1, item_classid,item_classname, item_lessonid,item_lessonname, item_teacherid,item_teachername)
                self.db.addClassLesson(_classlesson)
            else:
                _classlesson = ClassLesson(item_id, item_classid,item_classname, item_lessonid,item_lessonname, item_teacherid,item_teachername)
                self.db.editClassLesson(_classlesson)
        
    def delete_classlesson(self):
        selected_row_index = self.ui.tbl_classlesson.currentRow()
        print(selected_row_index)
        if selected_row_index >= 0:
            selected_id = self.ui.tbl_classlesson.item(selected_row_index, 0)
            self.db.deleteClassLesson(selected_id.text())
            self.load_classlessons()           
        else:
            QMessageBox.information(self, "Uyarı", "Lütfen ilk Önce Bir Satır Seçiniz ?", QMessageBox.Ok )




def app():
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = MenuWindow()
    mainMenu.show()

    sys.exit(app.exec_())

app()
