from create_connection import select_data
import colorama
from parsing_data import parsing_data


samples = """
 Hello! this is a menu of samples from the database
 1. 5 students with the highest average score in all subjects.
 2. 1 student with the highest average score in one subject.
 3. average score in a group for one subject.
 4. Current grade point average. - What courses does the teacher teach.
 5. List of students in the group.
 6. Grades of students in the subject group.
 7. Grades of students in the subject group in the last lesson.
 8. List of courses attended by the student.
 9. The list of courses that the teacher reads to the student. - The average score given by the teacher to the student.
 10. The average score given by the teacher.
"""

select1 = """
    SELECT  s.name, round(avg(grade), 2)
    FROM grades as g
    LEFT JOIN students as s on s.id = g.student_id
    GROUP BY s.name
    ORDER BY round(avg(grade), 2) desc
    limit 5
    """

select2 = """
    SELECT sub.subject as subject, stud.name as name, max(grade) as max_grade 
    FROM grades as g
    JOIN subjects as sub on g.subject_id = sub.id
    JOIN students as stud on g.subject_id = stud.id
    group by subject, name
    order by max_grade desc
    """

select3 = """
    SELECT gr.cluster, s.subject, round(avg(g.grade), 2)
    FROM grades as g
    LEFT JOIN group_for_student as gfs on gfs.student_id = g.student_id
    LEFT JOIN groups as gr on gfs.group_id = gr.id
    LEFT JOIN subjects as s on s.id = g.subject_id
    GROUP BY gr.cluster, s.subject
    ORDER BY gr.cluster asc
    """

select4 = """
    SELECT t.name, s.subject
    FROM grades g
    LEFT JOIN teachers_for_sub as t_f_s on t_f_s.subject_id = g.subject_id
    LEFT JOIN teachers as t on t.id = t_f_s.teacher_id
    LEFT JOIN subjects as s on s.id = g.subject_id
    GROUP BY t.name, s.subject
    ORDER BY t.name
    """

select5 = """
    SELECT s.name, gr.cluster
    FROM grades g
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN group_for_student as g_f_s on g_f_s.student_id = g.student_id
    LEFT JOIN groups as gr on gr.id = g_f_s.group_id
    GROUP BY s.name, gr.cluster
    ORDER BY gr.cluster
    """

select6 = """
    SELECT s.name, gr.cluster, sub.subject, g.grade
    FROM grades as g
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN group_for_student as g_f_s on g_f_s.student_id = g.student_id
    LEFT JOIN groups as gr on gr.id = g_f_s.group_id
    LEFT JOIN subjects as sub on sub.id = g.subject_id
    GROUP BY g.grade, s.name, gr.cluster, sub.subject
    ORDER BY s.name, gr.cluster, sub.subject
    """

select7 = """
    SELECT s.name, gr.cluster, sub.subject, g.grade, max(date_grade) as date_grade 
    FROM grades as g
    LEFT JOIN subjects as sub on sub.id = g.subject_id
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN group_for_student as g_f_s on g_f_s.student_id = g.student_id
    LEFT JOIN groups as gr on gr.id = g_f_s.group_id
    WHERE g.subject_id = 5
    GROUP BY s.name, gr.cluster, g.grade, sub.subject
    ORDER BY gr.cluster
    """

select8 = """
    SELECT s.name, sub.subject
    FROM grades as g 
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN subjects as sub on sub.id = g.subject_id
    GROUP BY s.name, sub.subject
    ORDER BY s.name
    """

select9 = """
    SELECT t.name, s.subject, round(avg(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN teachers_for_sub as t_f_s on t_f_s.subject_id = g.subject_id
    LEFT JOIN teachers as t on t.id = t_f_s.teacher_id
    LEFT JOIN subjects as s on s.id = g.subject_id
    GROUP BY t.name, s.subject
    ORDER BY round(avg(g.grade), 2) desc
    """

select10 = """
    SELECT t.name, round(avg(g.grade), 2)
    FROM grades g
    LEFT JOIN teachers_for_sub as t_f_s on t_f_s.subject_id = g.subject_id
    LEFT JOIN teachers as t on t.id = t_f_s.teacher_id
    GROUP BY t.name
    ORDER BY round(avg(g.grade), 2) desc
    """


list_selects = [select1, select2, select3, select4, select5, select6, select7, select8, select9, select10]


if __name__ == "__main__":
    while True:
        print(f'\033[36m {samples} \033[0m')
        input_data = input(
            f'\033[36m Please type the sample you want to receive from database(exit - end program): \033[0m')
        if input_data == 'exit':
            break
        print(parsing_data(input_data, select_data(list_selects[int(input_data) - 1])) + '\n')

