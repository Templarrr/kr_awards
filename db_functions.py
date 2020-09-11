import mysql.connector

from auth import DB_HOST, DB_LOGIN, DB_DATABASE_NAME, DB_PASSWORD

mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_LOGIN,
    password=DB_PASSWORD,
    database=DB_DATABASE_NAME
)


def get_awards_list(last_name=None, first_name=None, patronym=None):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("""
    SELECT award_date.award_date,
    people.people_last_name, people.people_first_name, people.people_patronym,
    award.award_name, award.award_type
    FROM award_date, people, award
    WHERE award_date.people_id = people.people_id
    AND award_date.award_id = award.award_id
    ORDER BY people.people_last_name, people.people_first_name, people.people_patronym, award_date.award_date
    """)
    data = cursor.fetchall()
    return data


def get_unique_last_names():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT people_last_name FROM people ORDER BY people_last_name")
    data = [record[0] for record in cursor.fetchall()]
    return data


def get_unique_first_names():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT people_first_name FROM people ORDER BY people_first_name")
    data = [record[0] for record in cursor.fetchall()]
    return data


def get_unique_patronyms():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT people_patronym FROM people ORDER BY people_patronym")
    data = [record[0] for record in cursor.fetchall()]
    return data


def get_unique_awards():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT award_name, award_id FROM award ORDER BY award_id")
    data = cursor.fetchall()
    return data
