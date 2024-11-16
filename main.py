from base import DataBase
connect = DataBase()

# 1 - 2

connect.create_courses()
connect.create_students()
connect.create_enrollments()
connect.create_teachers()
connect.create_course_assignments()

# 3

# ------------ Students ------------ #
connect.insert_students(17, 'toxir@gmail.com')
connect.insert_students(18, 'sobir@gmail.com')
connect.insert_students(19, 'bakir@gmail.com')
connect.insert_students(20, 'jalil@gmail.com')
connect.insert_students(21, 'ali@gmail.com')
connect.insert_students(22, 'vali@gmail.com')
connect.insert_students(22, 'bobur@gmail.com')

# ------------ Courses ------------ #

connect.insert_courses('PY123', 1)
connect.insert_courses('JS123', 5)
connect.insert_courses('NJ123', 2)

# ------------ Teachers ------------ #

connect.insert_teachers(6)
connect.insert_teachers(10)

# ------------ Assignments ------------ #

connect.insert_course_assignments(1, 2)
connect.insert_course_assignments(2, 3)

# 4

# connect.alter_table_students('students', 'talabalar')
# connect.alter_column_students('talabalar', 'age', 'student_age')

# 5

connect.update_data('talabalar','student_age', 10, 1)
connect.update_data('talabalar', 'student_age', 11, 2)

# 6

connect.delete_data('talabalar', 'student_id', 4)
connect.delete_data('talabalar', 'email', 'ali@gmail.com')