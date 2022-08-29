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

    adwa

### Author
[![GitHub Contributors Image](https://contrib.rocks/image?repo=LeadShadow/hw6web)](https://github.com/LeadShadow)

---
### License

[![GitHub](https://img.shields.io/github/license/LeadShadow/hw7web)](https://github.com/LeadShadow/hw7web/blob/main/LICENSE)