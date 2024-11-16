import psycopg2

class DataBase:
    def __init__(self):
        self.connect = psycopg2.connect(
            database='data',
            user='postgres',
            host='localhost',
            password='2007'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.connect as connect:
            result = None
            with connect.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    connect.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_students(self):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                age INTEGER CHECK(age > 0),
                email VARCHAR(100) UNIQUE NOT NULL
            );
        """
        self.manager(sql)

    def create_courses(self):
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                course_code VARCHAR(50) UNIQUE NOT NULL,
                credits INTEGER CHECK(credits >= 1 AND credits <= 5)
            );
        """
        self.manager(sql)

    def create_enrollments(self):
        sql = """
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
                course_id INTEGER REFERENCES courses(course_id) ON DELETE SET NULL
            );
        """
        self.manager(sql)

    def create_teachers(self):
        sql = """
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                experience_years INTEGER CHECK(experience_years >= 0)
            );
        """
        self.manager(sql)

    def create_course_assignments(self):
        sql = """
            CREATE TABLE IF NOT EXISTS course_assignments (
                assignment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE SET DEFAULT,
                course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE      
            );
        """
        self.manager(sql)

    def insert_students(self, age, email):
        sql = """
            INSERT INTO students (age, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;
        """
        self.manager(sql, age, email, commit=True)

    def insert_courses(self, code, credit):
        sql = """
            INSERT INTO courses (course_code, credits) VALUES (%s, %s) ON CONFLICT DO NOTHING;
        """
        self.manager(sql, code, credit, commit=True)

    def insert_teachers(self, year):
        sql = """
            INSERT INTO teachers (experience_years) VALUES (%s) ON CONFLICT DO NOTHING;
        """
        self.manager(sql, year, commit=True)

    def insert_course_assignments(self, teacher_id, course_id):
        sql = """
            INSERT INTO course_assignments (teacher_id, course_id) VALUES (%s, %s) ON CONFLICT DO NOTHING;
        """
        self.manager(sql, teacher_id, course_id, commit=True)

    def alter_table_students(self, old_name, new_name):
        sql = f"""
            ALTER TABLE {old_name} RENAME TO {new_name};
        """
        self.manager(sql, commit=True)

    def alter_column_students(self, table_name, old_column_name, new_column_name):
        sql = f"""
            ALTER TABLE {table_name} RENAME COLUMN {old_column_name} TO {new_column_name};
        """
        self.manager(sql, commit=True)

    def update_data(self, table_name, column_name, new_age, student_id):
        sql = f"""
            UPDATE {table_name} SET {column_name} = %s WHERE student_id = %s;
        """
        self.manager(sql, new_age, student_id, commit=True)

    def delete_data(self, table_name, column_name, value):
        sql = f"""
            DELETE FROM {table_name} WHERE {column_name} = %s;
        """
        self.manager(sql, value, commit=True)