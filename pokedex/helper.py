import sqlite3


class ConnectionWrapper:
    """A simple connection wrapper class"""

    def __init__(self):
        self.__conn = sqlite3.connect('../database.db')

    def get_all_pokemons(self):
        statement = "SELECT * FROM POKEDEX"
        return self.__conn.execute(statement).fetchall()

    def cleanup(self, should_close: bool):
        if should_close:
            self.__conn.close()


def fetch_all_pokemons():
    wrapper = ConnectionWrapper()
    return wrapper.get_all_pokemons()
