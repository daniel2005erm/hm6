import sqlite3
db = sqlite3.connect('txt.db')
a = db.cursor()
a.execute(""" CREATE TABLE IF NOT EXISTS user(
hobby text,
lastname text,
name text,
year_of_birth integer,
ball integer
)
""");

# students = [
#     ('John', 'Doe', 1990, 'Programming', 8),
#     ('Jane', 'Doe', 1991, 'Photography', 9),
#     ('Jim', 'Smith', 1992, 'Music', 7),
#     ('John', 'Smith', 1993, 'Art', 10),
#     ('Jane', 'Smith', 1994, 'Reading', 11),
#     ('Jim', 'Brown', 1995, 'Sport', 6),
#     ('John', 'Brown', 1996, 'Gaming', 12),
#     ('Jane', 'Brown', 1997, 'Writing', 13),
#     ('Jim', 'Wilson', 1998, 'Dancing', 5),
#     ('John', 'Wilson', 1999, 'Cooking', 14),
# ]

# for student in students:
#     a.execute("""
#     INSERT INTO user (name, lastname, year_of_birth, hobby, ball)
#     VALUES (?,?,?,?,?)
#     """, student)
a.execute("UPDATE user SET ball = 'gunius' WHERE ball >= 10")

a.execute("SELECT * FROM user  Where ball == 'gunius'")
item=a.fetchall()
for i in item:
    print(i)
a.execute("DELETE FROM user WHERE rowid % 2 == 0 ")
db.commit()
db.close()