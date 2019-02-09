#W hat is this package for

This package is intended to obtain the country an
IP address is located in as well as creating an
obfuscated id for the IP.

This package is intended to be used with the results
obtained from the result set posted to Amazon
DynamoDB by [SSH-Login-Attempts-Logger](https://github.com/PeterMcD/SSH-Login-Attempts-Logger)

## Setting up the package

The package relies on an API provided by ipstack.com
who offer free accounts with a generous allowance.

The package expects a config.py file with contents
similar to:

```python
api_base_url = "http://api.ipstack.com/"
api_key = ""
database_file = 'path/to/db'
```