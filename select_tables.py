from main import select_data
import colorama

# 1

select1 = """SELECT student_id , avg(grade) 
    FROM grades
    GROUP BY student_id
    ORDER BY avg desc 
    LIMIT 5;"""

# 2

select2 = """SELECT max(grade) as max_grade, sub.subject as subject, stud.name as name 
FROM grades as g
JOIN subjects AS sub ON g.subject_id = sub.id
JOIN students AS stud ON g.subject_id = stud.id
group by subject, name
order by max_grade DESC;"""

list_selects = [select1, select2]
if __name__ == "__main__":
    count = 0
    for select in list_selects:
        count += 1
        print(f'\033[32m Start {count} select in database\033[0m')
        select_data(select)
