from IpToCountry.ip_to_country import IpToCountry


class TestIpToCountry:
    def test_ip_to_country_config_parser(self):
        ip_to_country = IpToCountry()
        assert \
            ip_to_country._config['api']['url'] ==\
            'https://api.ipstack.com/'
        assert \
            ip_to_country._config['api']['key'] ==\
            'API_KEY'
        assert \
            ip_to_country._config['local']['database_file'] ==\
            r'..\resources\test_db'
