import random
from random import randint
from faker import Faker
from create_connection import create_connection
import colorama

fake = Faker()

groups = ['2КІ-21Б', '1КІ-21Б', '1СП-21Б']


subjects = ['Math', 'Chemistry', 'Physics', 'Geography', 'Biology']

dates = ['2022-02-14 08:15:00', '2022-02-15 10:15:00', '2022-02-16 12:00:00', '2022-02-16 14:00:00', '2022-02-17 10:00:00']


insert_into_students = "INSERT INTO students(name) VALUES(%s)"
insert_into_teachers = "INSERT INTO teachers(name) VALUES(%s)"
insert_into_subjects = "INSERT INTO subjects(subject) VALUES(%s)"
insert_into_groups = "INSERT INTO groups(cluster) VALUES(%s)"
insert_into_grades = "INSERT INTO grades(id, grade, student_id, subject_id, date_grade) VALUES(%s, %s, %s, %s, %s)"
insert_into_group_for_student = "INSERT INTO group_for_student(student_id, group_id) VALUES(%s, %s)"
insert_into_group_for_teachers = "INSERT INTO teachers_for_sub(teacher_id, subject_id) VALUES(%s, %s)"


def execute_simple_tables(cur, user_table, count, args=None):
    if user_table == insert_into_students or user_table == insert_into_teachers:
        for _ in range(count):
            cur.execute(user_table, (fake.name(),))
    if user_table == insert_into_subjects or user_table == insert_into_groups:
        for i in range(count):
            cur.execute(user_table, (args[i],))


def insert_into_tables(user_table, count):
    with create_connection() as conn:
        count_for_id = 0
        count_for_id_teacher = 0
        if conn is not None:
            cur = conn.cursor()
            if user_table == insert_into_students or user_table == insert_into_teachers:
                execute_simple_tables(cur, user_table, count)
            if user_table == insert_into_groups or user_table == insert_into_subjects:
                execute_simple_tables(cur, user_table, count, subjects if user_table == insert_into_subjects else groups)
            if user_table == insert_into_grades:
                for i in range(count):
                    if i % 5 == 0:
                        count_for_id += 1
                        count_for_id_teacher = 1
                    else:
                        count_for_id_teacher += 1
                    cur.execute(user_table, (count_for_id, randint(1, 12), count_for_id, count_for_id_teacher, dates[count_for_id_teacher-1]))

            if user_table == insert_into_group_for_student:
                for i in range(1, count+1):
                    cur.execute(user_table, (i, randint(1, 3)))
            if user_table == insert_into_group_for_teachers:
                for i in range(1, count+1):
                    if i < 3:
                        cur.execute(user_table, (1, i))
                    elif i < 5:
                        cur.execute(user_table, (2, i))
                    else:
                        cur.execute(user_table, (3, i))
            cur.close()
        else:
            print('Error: can\'t create the database connection')


insert_dict = {insert_into_students: 30, insert_into_teachers: 3, insert_into_subjects: 5, insert_into_groups: 3,
               insert_into_group_for_student: 30, insert_into_group_for_teachers: 5, insert_into_grades: 150}


if __name__ == "__main__":
    count = 0
    for k, v in insert_dict.items():
        count += 1
        print(f'\033[32mInserting into table - {count} some data\033[0m')
        insert_into_tables(k, v)
