import os
import pathlib
import sqlite3

DB_NAME = "kingdom_souls.sqlite3.db"
DB_PATH = pathlib.Path.joinpath(pathlib.Path.home(), DB_NAME)


class PrintableRow(sqlite3.Row):
    """Sqlite3 rows print as dicts for easy access."""

    def __str__(self):
        return str(dict(self))


def connect():
    """Connect to cached db."""
    if not connect.connection_cache:
        connect.connection_cache = sqlite3.connect(str(DB_PATH))
        connect.connection_cache.row_factory = PrintableRow
        # turn on foreign key option, which is needed for the cascade delete to work.
        connect.connection_cache.execute("PRAGMA foreign_keys=ON")
    return connect.connection_cache


connect.connection_cache = None


def prepare():
    """Prepare the database (create needed tables, indices, etc.)"""
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


def clear_table(name):
    """
    Clear the data of the specified table. For testing purposes.
    :param name: the table to clear
    """
    con = connect()
    with con:
        con.execute(f"""DELETE FROM {name}""")


def delete():
    """Delete the entire db. For testing purposes."""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
