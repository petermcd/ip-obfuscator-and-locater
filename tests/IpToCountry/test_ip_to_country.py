from IpToCountry.ip_to_country import IpToCountry


class Test_IpToCountry:
    def testParser(self):
        ip_to_country = IpToCountry()
        assert \
            ip_to_country._config['api']['url'] ==\
            'http://api.ipstack.com/'
        assert \
            ip_to_country._config['api']['key'] ==\
            'API_KEY'
        assert \
            ip_to_country._config['local']['database_file'] ==\
            r'..\resources\test_db'
