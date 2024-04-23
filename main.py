from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///education.db", echo=True)

create_students_table = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY NOT NULL,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    enrollment_year INTEGER
)
"""
insert_student = """
insert into students 
    (first_name, last_name, email, enrollment_year)
values ('Jacob', 'Grant', 'jacob@example.com', 2024)


"""

with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_student))
    conn.commit()
    result = conn.execute(text("select * from students"))
    print(result.all())