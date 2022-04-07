import re
import sqlite3


class ConnectionWrapper:
    """A simple connection wrapper class"""

    def __init__(self):
        self.__conn = sqlite3.connect('../database.db')

    def get_all_pokemons(self):
        statement = "SELECT * FROM POKEDEX"
        return self.__conn.execute(statement).fetchall()

    def register_subscriber(self, email):
        try:
            self.__conn.execute(f"INSERT into SUBSCRIBERS(email) values (?)", (email,))
            self.__conn.commit()
        except sqlite3.DatabaseError:
            ...
        except sqlite3.IntegrityError:
            ...

    def cleanup(self, should_close: bool):
        if should_close:
            self.__conn.close()


def fetch_all_pokemons():
    wrapper = ConnectionWrapper()
    return wrapper.get_all_pokemons()


def register_subscriber(email):
    pattern = re.compile(r'(\w|[a-zA-Z0-9_])+@\w+\.(com||ch)')
    if not pattern.match(email):
        raise "Invalid email!"
    wrapper = ConnectionWrapper()
    wrapper.register_subscriber(email)
    pass
