import requests
import json

import configparser

from IpToCountry.Dbh import Dbh
from IpToCountry.Dbh import DbhException


class IpToCountryException(Exception):
    pass


class IpToCountry:

    __slots__ = [
        '_config',
        '_dbh',
    ]

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read('IpToCountry/config.ini')
        self._dbh = None

    def get_ip_locations_from_database(self, database_file=None):
        """
        Iterates the database to ascertain the IP's country of origin.
        :param database_file: URL of the sqlite database to be iterated
        :raises ValueError: Raised when no database file supplied
        :return: None
        """
        if database_file is None:
            database_file = self._config['local']['database_file']
        if database_file is None:
            raise ValueError('Database file url not supplied')
        try:
            self._dbh = Dbh(database_file)
        except DbhException as ex:
            raise IpToCountryException(str(ex))
        for ip in self._dbh.fetch_ips():
            country = self.get_ip_location(ip)
            self._dbh.update_ip(ip, country)
        return None

    def get_ip_location(self, ip):
        """
        Queries an individual IP to ascertain the country.
        :param ip: IP to be queried.
        :raises ValueError: Raised if an invalid response is received.
        :raises ConnectionError: Raised if the API query failed..
        :return: country_name: name of the country the IP is associated with.
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
        IpToCountry = IpToCountry()
        IpToCountry.get_ip_locations_from_database()
    except IpToCountryException as ex:
        print(str(ex))
