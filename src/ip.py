import sqlite3
import requests
import json
import time

import config

ip_select_sql = "SELECT DISTINCT(`host`) FROM logins;"
ip_update_country_sql = "UPDATE logins SET `country` = ?, obfuscated_host = ? WHERE host = ?"

dbh = sqlite3.connect(config.database_file)
cursor = dbh.cursor()
cursor.execute(ip_select_sql)

hosts = cursor.fetchall()

i = 0

for host in hosts:
    url = config.api_base_url + host[0] + "?access_key=" + config.api_key
    request = requests.get(url)
    if request.status_code == 200:
        response = json.loads(request.text)
        cursor.execute(ip_update_country_sql, (response['country_name'], i, host[0]))
        time.sleep(0.5)
    i += 1

dbh.commit()
cursor.close()
dbh.close()
