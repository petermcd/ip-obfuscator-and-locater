## What is this package for

This package is intended to obtain the country an
IP address is located in as well as creating an
obfuscated id for the IP.

This package is intended to be used with the results
obtained from the result set posted to Amazon
DynamoDB by [SSH-Login-Attempts-Logger](https://github.com/PeterMcD/SSH-Login-Attempts-Logger)

## Setting up the package

The package relies on an API provided by [IP Stack](https://ipstack.com)
who offer free accounts with a generous allowance.

The package expects a config.ini file with contents
similar to:

```code
[api]
url = http://api.ipstack.com/
key = API_KEY
[local]
database_file = resources\test_db
```

The api key can be obtained from IP Stack after
signing up for an account.

THis package makes use of the requirements file.
Installing the requirements can be achieved from
calling the following command in the same folder
the requirements.txt file is in.

```code
pip install -r requirements.txt
```

## Usage

After configuration has been completed simply call
the script like:

```code
python IpToCountry.py
```

If you simply wish to ascertain the country for an
IP you can now add the following code:

```python
from IpToCountry import IpToCountry

ip_checker = IpToCountry()
print(ip_checker.get_ip_location('1.1.1.1'))
```

The above script would still require the ini file to be
configured for the url and api key however will not
attempt to write the results to a database.