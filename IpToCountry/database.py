"""Code to handle database connections and error handling."""
import sqlite3
from typing import Generator


class DatabaseException(Exception):
    """Exception class for database errors."""


class Database:
    """Class to handle database connections and queries."""

    __slots__ = ('_handler', '_cursor', '_unique_identifier')

    def __init__(self, database_file: str):
        """
        Initialize Database.

        Args:
             database_file: Location of the database file to open.
        """
        try:
            self._handler = sqlite3.connect(database=database_file)
        except sqlite3.OperationalError as exc:
            raise DatabaseException('Configured database file cannot be opened') from exc
        self._cursor = self._handler.cursor()
        self._unique_identifier = 0

    def update_ip(self, ip: str, country: str) -> None:
        """
        Update the IP details in the database.

        Args:
             ip: IP being queried.
             country: Country the IP is associated with
        """
        if not self._cursor:
            raise DatabaseException('Database cursor not initialised')
        sql = 'UPDATE logins '\
              'SET `country` = ?, `obfuscated_host` = ?'\
              ' WHERE `host` = ?'
        self._cursor.execute(sql, (country, self._unique_identifier, ip))
        self._unique_identifier += 1

    def fetch_ips(self) -> Generator[str, str, str]:
        """
        Iterate for the IP's in the database.

        Returns:
             Generator: IP, Country, Obfuscated Host
        """
        if not self._cursor:
            raise DatabaseException('Database cursor not initialised')
        sql = 'SELECT DISTINCT(`host`) FROM logins;'
        self._cursor.execute(sql)
        hosts = self._cursor.fetchall()
        for host in hosts:
            yield host[0]
        return ""

    def __del__(self) -> None:
        """Destructor."""
        if self._handler is not None:
            self._handler.commit()
            self._handler.close()
        return None
