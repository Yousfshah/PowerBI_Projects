import mysql.connector
from sqlalchemy import create_engine

class MySQLManager:
    def __init__(self, host="localhost", port=3307, user="root", password="Mohammad786"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()

    def create_database(self, db_name):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    def show_databases(self):
        self.cursor.execute("SHOW DATABASES")
        print("Available Databases:")
        for db in self.cursor:
            print(" -", db[0])

    def get_sqlalchemy_engine(self, database):
        url = f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{database}"
        return create_engine(url)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()