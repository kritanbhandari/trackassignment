import sqlite3


class TableDatabase:
    def __init__(self, connection, table_name, cursor):
        self.table_name = table_name
        self.cursor = cursor
        self.connection = connection

    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {self.table_name}(
                                ID INTEGER PRIMARY KEY NOT NULL,
                                SUBJECT CHAR(50) NOT NULL,
                                ASSIGNMENT_NAME TEXT UNIQUE,
                                ASSIGNMENT_DUE_DATE timestamp, 
                                ASSIGNMENT_SUBMITTED_DATE timestamp,
                                ASSIGNMENT_SCORE CHAR(25),
                                ASSIGNMENT_LINK TEXT
                                );"""
        with self.connection:
            self.cursor.execute(query)

    def insert_assignment(
        self,
        subject,
        assignment_name,
        assignment_due_date,
        assignment_submitted_date,
        assignment_score,
        assignment_link,
    ):
        query = f"""
        INSERT INTO {self.table_name} 
        (SUBJECT, ASSIGNMENT_NAME, ASSIGNMENT_DUE_DATE,
        ASSIGNMENT_SUBMITTED_DATE, ASSIGNMENT_SCORE, ASSIGNMENT_LINK) 
        VALUES ("{subject}", "{assignment_name}", "{assignment_due_date}", 
        "{assignment_submitted_date}", "{assignment_score}", "{assignment_link}"
        );"""

        with self.connection:
            self.cursor.execute(query)

    def drop_table(self):
        query = f"""DROP TABLE {self.table_name}"""
        self.connection.execute(query)

    def query_rows(self):
        query = f"SELECT * FROM {self.table_name}"
        return self.connection.execute(query).fetchall()


class UsersTable:

    def __init__(self, connection, table_name, cursor):
        self.table_name = table_name
        self.cursor = cursor
        self.connection = connection

    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {self.table_name}(
                                ID INTEGER PRIMARY KEY NOT NULL,
                                USERNAME CHAR(50) NOT NULL,
                                PASSWORD CHAR(50) NOT NULL,
                                );"""
        with self.connection:
            self.cursor.execute(query)

    def insert_assignment(self, username, password):
        query = f"""
        INSERT INTO {self.table_name} 
        (USERNAME, PASSWORD) 
        VALUES ("{username}", "{password}"
        );"""

        with self.connection:
            self.cursor.execute(query)

    def drop_table(self):
        query = f"""DROP TABLE {self.table_name}"""
        self.connection.execute(query)

    def query_rows(self):
        query = f"SELECT * FROM {self.table_name}"
        return self.connection.execute(query).fetchall()


if __name__ == "__main__":
    connection = sqlite3.connect("table_data.db")
    cursor = connection.cursor()
    new_table = TableDatabase(connection, "Assignments", cursor=cursor)
    new_table.drop_table()
    # new_table.create_table()

    # new_table.drop_table()
    # print(new_table.query_rows())
    # new_table.drop_table()
    # # new_table.drop_table()
    # # new_table.create_table()
    # # date = convert_date("2024 Aug 21  11am")
    # # new_table.insert_assignment("Composition", "Ethos", date, date, "10", "https://youtube.com" )
    # print(new_table.query_rows())
