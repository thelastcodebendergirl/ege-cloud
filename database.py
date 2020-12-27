import psycopg2
import json

from config import Configuration


class Database:
    def __init__(self):
        self.config = Configuration("config.json").config["database"]
        self.connection = psycopg2.connect("host={0} port={1} user={2} dbname={3} password={4} sslmode={5}"
                                           .format(self.config["host"],
                                                   self.config["port"],
                                                   self.config["user"],
                                                   self.config["dbname"],
                                                   self.config["password"],
                                                   self.config["ssl"]))

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()