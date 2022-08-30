# *Hw8Web*

### Database 'postgres' that contains students, groups, subjects specified by the teacher and grades from subjects
#### Creating and inserting using Python scripts

[![Language](https://img.shields.io/badge/language-python-blue?&style=plastic)](https://www.python.org)
[![Language version](https://img.shields.io/badge/version-3.10-red?&style=plastic)](https://www.python.org/downloads/)
![GitHub repo size](https://img.shields.io/badge/repo%20size-39%20kB-pink?&style=plastic)

---

### Technology which used:
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://github.com/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://git-scm.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

---

***We have 30 students, 3 groups, 5 subjects, 3 teachers and 5 grades each student has***

Module create_table -> creates table

Module insert_table -> inserts into tables different values

Module main -> contains connect with database


### Ok let's move on to samplings from the database
Our tasks:

* 5 students with the highest average score in all subjects.
* 1 student with the highest average score in one subject.
* average score in a group for one subject.
* Current grade point average. - What courses does the teacher teach.
* List of students in the group.
* Grades of students in the subject group.
* Grades of students in the subject group in the last lesson.
* List of courses attended by the student.
* The list of courses that the teacher reads to the student. - The average score given by the teacher to the student.
* The average score given by the teacher.
<p align="center">1</p>

    SELECT student_id , avg(grade) 
    FROM grades
    GROUP BY student_id
    ORDER BY avg desc 
    LIMIT 5;

<p align="center">2</p>

    SELECT sub.subject as subject, stud.name as name, max(grade) as max_grade 
    FROM grades as g
    JOIN subjects as sub on g.subject_id = sub.id
    JOIN students as stud on g.subject_id = stud.id
    group by subject, name
    order by max_grade desc

<p align="center">3</p>

    SELECT gr.cluster, s.subject, avg(g.grade)
    FROM grades as g
    LEFT JOIN group_for_student as gfs on gfs.student_id = g.student_id
    LEFT JOIN groups as gr on gfs.group_id = gr.id
    LEFT JOIN subjects as s on s.id = g.subject_id
    GROUP BY gr.cluster, s.subject
    ORDER BY gr.cluster asc

<p align="center">4</p>

    SELECT t.name, s.subject
    FROM grades g
    LEFT JOIN teachers_for_sub as t_f_s on t_f_s.subject_id = g.subject_id
    LEFT JOIN teachers as t on t.id = t_f_s.teacher_id
    LEFT JOIN subjects as s on s.id = g.subject_id
    GROUP BY t.name, s.subject
    ORDER BY t.name

<p align="center">5</p>

    SELECT s.name, gr.cluster
    FROM grades g
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN group_for_student as g_f_s on g_f_s.student_id = g.student_id
    LEFT JOIN groups as gr on gr.id = g_f_s.group_id
    GROUP BY s.name, gr.cluster
    ORDER BY gr.cluster

<p align="center">6</p>

    SELECT s.name, gr.cluster, sub.subject, g.grade
    FROM grades as g
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN group_for_student as g_f_s on g_f_s.student_id = g.student_id
    LEFT JOIN groups as gr on gr.id = g_f_s.group_id
    LEFT JOIN subjects as sub on sub.id = g.subject_id
    GROUP BY g.grade, s.name, gr.cluster, sub.subject
    ORDER BY s.name, gr.cluster, sub.subject

<p align="center">7</p>

    SELECT s.name, gr.cluster, sub.subject, g.grade, max(date_grade) as date_grade
    FROM grades as g
    LEFT JOIN subjects as sub on sub.id = g.subject_id
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN group_for_student as g_f_s on g_f_s.student_id = g.student_id
    LEFT JOIN groups as gr on gr.id = g_f_s.group_id
    WHERE g.subject_id = 5
    GROUP BY s.name, gr.cluster, g.grade, sub.subject
    ORDER BY gr.cluster

<p align="center">8</p>

    SELECT s.name, sub.subject
    FROM grades as g 
    LEFT JOIN students as s on s.id = g.student_id
    LEFT JOIN subjects as sub on sub.id = g.subject_id
    GROUP BY s.name, sub.subject
    ORDER BY s.name

<p align="center">9</p>

    SELECT t.name, s.subject, round(avg(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN teachers_for_sub as t_f_s on t_f_s.subject_id = g.subject_id
    LEFT JOIN teachers as t on t.id = t_f_s.teacher_id
    LEFT JOIN subjects as s on s.id = g.subject_id
    GROUP BY t.name, s.subject
    ORDER BY round(avg(g.grade), 2) desc

<p align="center">10</p>

    SELECT t.name, round(avg(g.grade), 2)
    FROM grades g
    LEFT JOIN teachers_for_sub as t_f_s on t_f_s.subject_id = g.subject_id
    LEFT JOIN teachers as t on t.id = t_f_s.teacher_id
    GROUP BY t.name
    ORDER BY round(avg(g.grade), 2) desc

### Author
[![GitHub Contributors Image](https://contrib.rocks/image?repo=LeadShadow/hw8web)](https://github.com/LeadShadow)

---
### License

[![GitHub](https://img.shields.io/github/license/LeadShadow/hw8web)](https://github.com/LeadShadow/hw8web/blob/main/LICENSE)