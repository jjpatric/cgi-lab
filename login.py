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

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_auth = cookie_username == secret.username and cookie_password == secret.password

if cookie_auth:
    username = cookie_username
    password = cookie_password

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