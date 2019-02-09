## What is this package for

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

The api key can be obtained from ipstack after
signing up for an account.

If you do not already have the Requests package
installed you will also need to install this such as

```python
pip install requests
```

## Usage

After configuration has been completed simply call
the script like:

```python
python ip.py
```

As is the script waits for 1/2 a second after each
api request so that the API is not overloaded with
requests.