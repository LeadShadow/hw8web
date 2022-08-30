from create_connection import create_context_connection
import colorama


table_groups = """CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY NOT NULL,
    cluster VARCHAR(50)
)"""

table_students = """CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50)
)"""

table_teachers = """CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50)
)"""

table_subjects = """CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY NOT NULL,
    subject VARCHAR(50)
)"""

table_group_for_student = """CREATE TABLE IF NOT EXISTS group_for_student (
    id SERIAL PRIMARY KEY NOT NULL,
    student_id INTEGER,
    group_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (group_id) REFERENCES groups(id)
)"""

table_group_for_teachers = """CREATE TABLE IF NOT EXISTS teachers_for_sub (
    id SERIAL PRIMARY KEY NOT NULL,
    teacher_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)"""

table_grades = """CREATE TABLE IF NOT EXISTS grades (
    id INTEGER,
    grade INTEGER,
    student_id INTEGER,
    subject_id INTEGER,
    date_grade TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)"""

list_of_tables = [table_groups, table_students, table_teachers, table_subjects, table_group_for_student, table_group_for_teachers, table_grades]

if __name__ == "__main__":
    count = 0
    for i in list_of_tables:
        count += 1
        print(f'\033[32mCreate table {count}\033[0m')
        create_context_connection(i)

