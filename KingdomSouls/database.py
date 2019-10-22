import os
import pathlib
import sqlite3

DB_NAME = "kingdom_souls.sqlite3.db"
DB_PATH = pathlib.Path.joinpath(pathlib.Path.home(), DB_NAME)


class PrintableRow(sqlite3.Row):
    def __str__(self):
        return str(dict(self))


def connect():
    if not connect.connection_cache:
        connect.connection_cache = sqlite3.connect(str(DB_PATH))
        connect.connection_cache.row_factory = PrintableRow
        # turn on foreign key option, which is needed for the cascade delete to work.
        connect.connection_cache.execute("PRAGMA foreign_keys=ON")
    return connect.connection_cache


connect.connection_cache = None


def prepare():
    con = connect()
    with con:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS characters (
                name string primary key,
                attack int,
                defense int
            )
        """
        )


def delete():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
