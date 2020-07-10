#!/usr/bin/env python3

import http.client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection
from huawei_lte_api.Client import Client

URL = "http://192.168.8.1/"
USERNAME = "admin"
PASSWORD = "jah56789S"
CONNECTION_TIMEOUT = 10

http.client.HTTPConnection.debuglevel = 1

if USERNAME or PASSWORD:
    connection = AuthorizedConnection(
        URL, username=USERNAME, password=PASSWORD, timeout=CONNECTION_TIMEOUT
    )
else:
    connection = Connection(URL, timeout=CONNECTION_TIMEOUT)

if isinstance(connection, AuthorizedConnection):
    print(Client(connection).device.information())
    Client(connection).user.logout()

