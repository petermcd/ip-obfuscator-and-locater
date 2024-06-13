"""Code to handle translation of IP addresses to countries."""
import configparser
import json
from typing import Optional

import requests

from IpToCountry.database import Database, DatabaseException


class IpToCountryException(Exception):
    """Exception raised for errors in the IpToCountry class."""

    pass


class IpToCountry:
    """Class to handle translation of IP addresses to countries."""

    __slots__ = [
        '_config',
        '_handler',
    ]

    def __init__(self):
        """Initialize the class."""
        self._config = configparser.ConfigParser()
        self._config.read('IpToCountry/config.ini')
        self._handler = None

    def get_ip_locations_from_database(self, database_file: Optional[str] = None) -> None:
        """
        Iterate the database to ascertain the IP's country of origin.

        Args:
             database_file: URL of the sqlite database to be iterated
        Raises:
             ValueError: Raised when no database file supplied
        """
        if not database_file:
            database_file = self._config['local']['database_file']
        if not database_file:
            raise IpToCountryException('No database file supplied')
        try:
            self._handler = Database(database_file)
        except DatabaseException as exc:
            raise IpToCountryException(str(exc))
        for ip in self._handler.fetch_ips():
            country = self.get_ip_location(ip)
            self._handler.update_ip(ip, country)

    def get_ip_location(self, ip: str) -> str:
        """
        Query an individual IP to ascertain the country.

        Args:
             ip: IP to be queried.
        Raises:
             ValueError: Raised if an invalid response is received.
             ConnectionError: Raised if the API query failed.
        Returns: country_name: name of the country the IP is associated with.
        """
        url = \
            self._config['api']['url']\
            + ip \
            + "?access_key=" \
            + self._config['api']['key']
        request = requests.get(url)
        if request.status_code == 200:
            response = json.loads(request.text)
            '''
            The success key only appears in the response
            if the query returned an error
            '''
            if 'success' in response and not response['success']:
                raise IpToCountryException(response)
            else:
                return response['country_name']
        else:
            raise IpToCountryException('Connection failed')


if __name__ == '__main__':
    try:
        ip_to_country = IpToCountry()
        ip_to_country.get_ip_locations_from_database()
    except IpToCountryException as ex:
        print(str(ex))
