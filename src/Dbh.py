import sqlite3


class Dbh:

    def __init__(self, database):
        """
        Constructor
        :param database: Location of the database file to open.
        """
        self._handler = sqlite3.connect(database=database)
        self._cursor = self._handler.cursor()
        self._unique_identifier = 0

    def update_ip(self, ip, country):
        """
        Updates the IP details in the database.
        :param ip: IP being queried.
        :param country: Country the IP is associated with
        :return: None
        """
        sql = 'UPDATE logins SET `country` = ?, `obfuscated_host` = ? WHERE `host` = ?'
        self._cursor.execute(sql, (country, self._unique_identifier, ip))
        self._unique_identifier += 1
        return None

    def fetch_ips(self):
        """
        Iterator for the IP's in the database
        :return: IP
        """
        sql = 'SELECT DISTINCT(`host`) FROM logins;'
        self._cursor.execute(sql)
        hosts = self._cursor.fetchall()
        for host in hosts:
            yield host[0]

    def __del__(self):
        """
        Destructor
        :return: None
        """
        self._handler.commit()
        self._handler.close()
        return None
