CREATE OR REPLACE PACKAGE PYTHONORA.SCHOOL_PKG AS

/**** STUDENTS OPERATIONS BEGIN**/

TYPE STUDENT_REC IS RECORD (
   STUDENT_ID NUMBER(6),
   STUDENT_NUMBER VARCHAR2(10),
   NAME VARCHAR2(20),
   SURNAME VARCHAR2(20),
   BIRTHDATE DATE,
   GENDER VARCHAR2(5),
   CLASS_ID NUMBER(6)
);
TYPE STUDENT_CURS IS REF CURSOR RETURN STUDENT_REC;

FUNCTION GET_STUDENTS_BYID(STUDENT_ID1 IN NUMBER) RETURN STUDENT_CURS;

FUNCTION GET_STUDENTS_BYCLASSID(CLASS_ID1 IN NUMBER) RETURN STUDENT_CURS;

FUNCTION GET_ALL_STUDENTS(STUDENT_ID1 IN NUMBER,CLASS_ID1 IN NUMBER) RETURN STUDENT_CURS;

FUNCTION STUDENT_PUT(STUDENT_NUMBER1 VARCHAR2,
                     NAME1 VARCHAR2,
                     SURNAME1 VARCHAR2,
                     BIRTHDATE1 DATE,
                     GENDER1 VARCHAR2,
                     CLASS_ID1 NUMBER) RETURN NUMBER;

FUNCTION STUDENT_UPDATE(STUDENT_ID1 NUMBER,
                        STUDENT_NUMBER1 VARCHAR2,
                        NAME1 VARCHAR2,
                        SURNAME1 VARCHAR2,
                        BIRTHDATE1 DATE,
                        GENDER1 VARCHAR2,
                        CLASS_ID1 NUMBER) RETURN NUMBER;

PROCEDURE STUDENT_DELETE(STUDENT_ID1 IN NUMBER);
  
/**** STUDENTS OPERATIONS END**/

/**** TEACHERS OPERATIONS BEGIN**/

TYPE TEACHER_REC IS RECORD (
   TEACHER_ID NUMBER(6),
   BRANCH VARCHAR2(25),
   NAME VARCHAR2(35),
   SURNAME VARCHAR2(35),
   BIRTHDATE DATE,
   GENDER VARCHAR2(5)
);
TYPE TEACHER_CURS IS REF CURSOR RETURN TEACHER_REC;

FUNCTION GET_TEACHER_BY_ID(TEACHER_ID1 IN NUMBER) RETURN TEACHER_CURS;

FUNCTION GET_TEACHERS_BY_BRANCH(BRANCH1 IN VARCHAR2) RETURN TEACHER_CURS;

FUNCTION GET_ALL_TEACHERS(TEACHER_ID1 IN NUMBER,BRANCH1 IN VARCHAR2) RETURN TEACHER_CURS;

FUNCTION TEACHER_PUT(NAME1 VARCHAR2,
                     SURNAME1 VARCHAR2,
                     BIRTHDATE1 DATE,
                     GENDER1 VARCHAR2,
                     BRANCH1 VARCHAR2) RETURN NUMBER;

FUNCTION TEACHER_UPDATE(TEACHER_ID1 NUMBER,
                        NAME1 VARCHAR2,
                        SURNAME1 VARCHAR2,
                        BIRTHDATE1 DATE,
                        GENDER1 VARCHAR2,
                        BRANCH1 VARCHAR2) RETURN NUMBER;

PROCEDURE TEACHER_DELETE(TEACHER_ID1 IN NUMBER);

/**** TEACHERS OPERATIONS END**/

/**** CLASSES OPERATIONS BEGIN**/

TYPE CLASS_REC IS RECORD (
   CLASS_ID NUMBER(6),
   NAME VARCHAR2(35),
   TEACHER_ID NUMBER(6)
);
TYPE CLASS_CURS IS REF CURSOR RETURN CLASS_REC;

FUNCTION GET_CLASS_BY_ID(CLASS_ID1 IN NUMBER) RETURN CLASS_CURS;

FUNCTION GET_CLASSES_BY_TEACHERID(TEACHER_ID1 IN NUMBER) RETURN CLASS_CURS;

FUNCTION GET_ALL_CLASSES(CLASS_ID1 IN NUMBER,TEACHER_ID1 IN NUMBER) RETURN CLASS_CURS;

FUNCTION CLASS_PUT(NAME1 VARCHAR2,
                   TEACHER_ID1 NUMBER) RETURN NUMBER;

FUNCTION CLASS_UPDATE(CLASS_ID1 NUMBER,
                      NAME1 VARCHAR2,
                      TEACHER_ID1 NUMBER) RETURN NUMBER;

PROCEDURE CLASS_DELETE(CLASS_ID1 IN NUMBER);

/**** CLASSES OPERATIONS END**/

/**** LESSONS OPERATIONS BEGIN**/

TYPE LESSON_REC IS RECORD (
   LESSON_ID NUMBER(6),
   NAME VARCHAR2(35)
);
TYPE LESSON_CURS IS REF CURSOR RETURN LESSON_REC;

FUNCTION GET_LESSON_BY_ID(LESSON_ID1 IN NUMBER) RETURN LESSON_CURS;

FUNCTION GET_LESSONS_BY_NAME(NAME1 IN VARCHAR2) RETURN LESSON_CURS;

FUNCTION GET_ALL_LESSONS(LESSON_ID1 IN NUMBER,NAME1 IN VARCHAR2) RETURN LESSON_CURS;

FUNCTION LESSON_PUT(NAME1 VARCHAR2) RETURN NUMBER;

FUNCTION LESSON_UPDATE(LESSON_ID1 NUMBER,
                       NAME1 VARCHAR2) RETURN NUMBER;

PROCEDURE LESSON_DELETE(LESSON_ID1 IN NUMBER);

/**** LESSONS OPERATIONS END**/

/**** CLASSES-LESSONS OPERATIONS BEGIN**/

TYPE CLASS_LESSON_REC IS RECORD (
   ID NUMBER(6),
   CLASS_ID NUMBER(6),
   CLASS_NAME VARCHAR2(35),
   LESSON_ID NUMBER(6),
   LESSON_NAME VARCHAR2(35),
   TEACHER_ID NUMBER(6),
   TEACHE_NAME VARCHAR2(35)
);
TYPE CLASS_LESSON_CURS IS REF CURSOR RETURN CLASS_LESSON_REC;

FUNCTION GET_CLASSLESSON_BY_ID(ID1 IN NUMBER) RETURN CLASS_LESSON_CURS;

FUNCTION GET_ALL_CLASSLESSONS(ID1 IN NUMBER,
                              CLASS_ID1 IN NUMBER,
                              CLASS_NAME1 IN VARCHAR2,
                              LESSON_ID1 IN NUMBER,
                              LESSON_NAME1 IN VARCHAR2,
                              TEACHER_ID1 IN NUMBER,
                              TEACHER_NAME1 IN VARCHAR2) RETURN CLASS_LESSON_CURS;

FUNCTION CLASS_LESSON_PUT(CLASS_ID1 IN NUMBER,
                          LESSON_ID1 IN NUMBER,
                          TEACHER_ID1 IN NUMBER) RETURN NUMBER;

FUNCTION CLASS_LESSON_UPDATE(ID1 IN NUMBER,
                             CLASS_ID1 IN NUMBER,
                             LESSON_ID1 IN NUMBER,
                             TEACHER_ID1 IN NUMBER) RETURN NUMBER;

PROCEDURE CLASS_LESSON_DELETE(ID1 IN NUMBER);

/**** CLASSES-LESSONS OPERATIONS END**/



END SCHOOL_PKG;
/