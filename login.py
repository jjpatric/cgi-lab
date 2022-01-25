#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")



print("Content-Type: text/html")

if not username and not password:
    print()
    print(login_page())
elif username == secret.username and password == secret.password:
    C = SimpleCookie()
    C["username"] = username
    C["password"] = password
    print(C)
    print()
    print(secret_page(username, password))
else:
    print()
    print(after_login_incorrect())